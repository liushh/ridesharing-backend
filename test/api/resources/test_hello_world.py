import falcon
from sure import expect

from test import TestCase


class TestHelloWorld(TestCase):
    def test_hello_world_get(self):
        response = self.simulate_get('/hello_world')

        expect(response.status).to.equal(falcon.HTTP_OK)
