import json
from json.decoder import JSONDecodeError

import falcon


class JSONMiddleware:
    def process_resource(self, req, resp, resource, params):
        print('JSONMiddleware process_resource')
        if self._is_middleware_enabled(resource) and self._request_method_has_payload(req):
            print('_is_middleware_enabled  and _request_method_has_payload')
            if not self._is_json_content_type(req):
                print('false from _is_json_content_type')
                raise falcon.HTTPUnsupportedMediaType()

            print('great content')
            try:
                req.text = self._get_payload(req)
                print('req.text = ', req.text)
                req.json = json.loads(req.text)
                print('req.json = ', req.json)
            except JSONDecodeError:
                print('JSON decode error!!!!!!!!!!!!!!!!')
                raise falcon.HTTPInternalServerError()

    def _is_middleware_enabled(self, resource):
        return not hasattr(resource, 'disable_json_middleware') \
            or not resource.disable_json_middleware

    def _request_method_has_payload(self, req):
        return req.method in ('POST', 'PATCH')

    def _is_json_content_type(self, req):
        return req.content_type in ['application/json', 'text/json']

    def _get_payload(self, req):
        return req.bounded_stream.read().decode('utf-8')

    def process_response(self, req, resp, resource, req_succeeded):
        if not self._has_body(resp):
            resp.body = self._serialize_json_to_string(resp)

    def _has_body(self, resp):
        return resp.body is not None

    def _serialize_json_to_string(self, resp):
        if self._has_json(resp):
            if not isinstance(resp.json, dict) and \
               not isinstance(resp.json, list):
                raise falcon.HTTPInternalServerError()
            return json.dumps(resp.json)
        return json.dumps({})

    def _has_json(self, resp):
        return hasattr(resp, 'json')
