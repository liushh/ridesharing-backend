import falcon

from api import HelloWorldResource
from database import Database
from middlewares.database import DatabaseMiddleware


class App(falcon.API):
    def __init__(self, config, *args, **kwargs):
        self._database = Database(config)

        kwargs['middleware'] = self._get_middlewares(config)
        super(App, self).__init__(*args, **kwargs)

        self._configure_routes()

    def _configure_routes(self):
        self.add_route('/hello_world', HelloWorldResource())
        self.add_route('/', HelloWorldResource())

    def _get_middlewares(self, config):
        database = DatabaseMiddleware(self._database)

        return [database]

    def get_database(self):
        return self._database
