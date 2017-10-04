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
        if req.method == 'OPTIONS':
            return

        strategy = getattr(resource, 'auth', AuthStrategy.WITH_JWT)

        if strategy == AuthStrategy.WITH_JWT:
            return self.jwt_middleware.process_resource(req, resp, resource, params)
        elif strategy == AuthStrategy.WITHOUT_AUTHENTICATION:
            return
        else:
            raise falcon.HTTPUnauthorized
