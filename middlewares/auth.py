from enum import Enum

import falcon


class AuthStrategy(Enum):
    WITH_JWT = 1
    WITH_CLIENT_SECRET = 2
    WITHOUT_AUTHENTICATION = 3


class AuthMiddleware:
    def __init__(self, jwt_middleware):
        self.jwt_middleware = jwt_middleware

    def process_resource(self, req, resp, resource, params):
        # OPTIONS method is used by browsers as part of CORS mechanism. We can
        # safely bypass authentication for this method.
        print('AuthStrategy process_resource')
        if req.method == 'OPTIONS':
            print('option request~ do nothing')
            return

        print('resource = ', resource)
        strategy = getattr(resource, 'auth', AuthStrategy.WITH_JWT)

        print('strategy = ', strategy)
        if strategy == AuthStrategy.WITH_JWT:
            print('sending to jwt middleware')
            return self.jwt_middleware.process_resource(req, resp, resource, params)
        elif strategy == AuthStrategy.WITHOUT_AUTHENTICATION:
            print('without authentication')
            return
        else:
            raise falcon.HTTPUnauthorized
