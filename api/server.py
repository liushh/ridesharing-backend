import falcon

from api import HelloWorldResource


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self._configure_routes()

    def _configure_routes(self):
        self.add_route('/hello_world', HelloWorldResource())
