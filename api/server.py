import falcon
from falcon_cors import CORS

from api.resources import HelloWorldResource
from api.resources import UsersResource
from api.resources import SpaceResource
from database import Database
from middlewares.database import DatabaseMiddleware
from middlewares.json import JSONMiddleware
from middlewares.jwt import JWTMiddleware, Auth0UserCreator
from middlewares.auth import AuthMiddleware


class App(falcon.API):
    def __init__(self, config, *args, **kwargs):
        self._database = Database(config)

        kwargs['middleware'] = self._get_middlewares(config)
        super(App, self).__init__(*args, **kwargs)

        self._configure_routes()

    def _configure_routes(self):
        self.add_route('/hello_world', HelloWorldResource())

        self.add_route('/api/user', UsersResource())

        self.add_route('/api/space/', SpaceResource())
        self.add_route('/api/space/{space_id}', SpaceResource())

        self.add_route('/api/spaces/{office_id}', SpaceResource())

    def _get_middlewares(self, config):
        database = DatabaseMiddleware(self._database)
        json = JSONMiddleware()
        cors = self._get_cors_middleware(config)
        auth = self._get_auth_middleware(config)

        return [cors, auth, database, json]

    def get_database(self):
        return self._database

    def _get_cors_middleware(self, config):
        cors_options = {
            'allow_all_methods': True,
            'allow_headers_list': ['content-type', 'authorization']
        }

        if config.CORS_ORIGIN == '*':
            cors_options['allow_all_origins'] = True
            print('allow_all_origins!!!!!!!!!!!!!!!!!!')
        elif isinstance(config.CORS_ORIGIN, str):
            cors_options['allow_origins_list'] = [config.CORS_ORIGIN]
        elif isinstance(config.CORS_ORIGIN, list):
            cors_options['allow_origins_list'] = config.CORS_ORIGIN

        cors = CORS(**cors_options)

        return cors.middleware

    def _get_auth_middleware(self, config):
        def has_valid_value(config_name):
            value = getattr(config, config_name, None)
            return value is not None and value != ''

        if not has_valid_value('AUTH0_CLIENT_SECRET'):
            raise Exception('Please set a valid Auth0 client secret (AUTH0_CLIENT_SECRET)')

        if not has_valid_value('AUTH0_CLIENT_ID'):
            raise Exception('Please set a valid Auth0 client id (AUTH0_CLIENT_ID)')

        if not has_valid_value('AUTH0_AUDIENCE'):
            raise Exception('Please set a valid Auth0 audience (AUTH0_AUDIENCE)')

        if not has_valid_value('AUTH0_ISSUER'):
            raise Exception('Please set a valid Auth0 issuer (AUTH0_ISSUER)')

        if not has_valid_value('AUTH0_DOMAIN'):
            raise Exception('Please set a valid Auth0 domain (AUTH0_DOMAIN)')

        jwt = JWTMiddleware(
            self._database,
            config.AUTH0_CLIENT_SECRET,
            config.AUTH0_AUDIENCE,
            config.AUTH0_ISSUER
        )

        return AuthMiddleware(jwt)
