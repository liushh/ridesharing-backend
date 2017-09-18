# flake8: noqa
from falcon import testing

from config import Test
from api.server import App


class TestCase(testing.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.app = App(Test)
