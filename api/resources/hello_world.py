import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Hello World!')
