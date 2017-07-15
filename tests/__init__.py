# flake8: noqa
from falcon import testing

from api.server import App


class TestCase(testing.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.app = App()
