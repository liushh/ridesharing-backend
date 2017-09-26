import falcon
from sure import expect

from tests import TestCase


class TestTrips(TestCase):
    def test_get_all_trips(self):
        response = self.simulate_get('/api/trips')

        expect(response.status).to.equal(falcon.HTTP_OK)
        expect(response.json).to.equal({})
