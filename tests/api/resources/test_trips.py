from datetime import datetime

import falcon
from sure import expect

from tests import TestCase


class TestTrips(TestCase):
    def test_get_all_trips(self):
        response = self.simulate_get('/api/trips')
        expected_trip = {
            'id': 1,
            'driveOrRide': 'Drive',
            'origin': {
                'isOffice': False,
                'zipcode': 'NW1 6XE',
                'colony': 'Marylebone',
            },
            'destination': {
                'isOffice': False,
                'zipcode': '31351',
                'colony': '-',
            },
            'time': datetime(1992, 9, 4).strftime('%s')
        }

        expect(response.status).to.equal(falcon.HTTP_OK)
        expect(response.json).to.equal(expected_trip)
