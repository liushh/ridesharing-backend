from dateutil import parser
import json

import falcon
from sure import expect

from test import TestCase


class TestTrips(TestCase):
    VALID_TRIP_PAYLOAD = {
        'email': 'liusha@wizeline.com',
        'phone': '12345678',
        'driveOrRide': 'Drive',
        'time': '2016-10-19T20:17:52.2891902Z',
        'origin': {
            'isOffice': False,
            'zipcode': 'NW1 6XE',
            'colonyOrDistrict': '-'
        },
        'destination': {
            'isOffice': False,
            'zipcode': 'NW1 6XE',
            'colonyOrDistrict': '-'
        }
    }

    def test_get_all_trips(self):
        response = self.simulate_get('/api/trips')
        expected_trips = [{
            'id': 1,
            'driveOrRide': 'Drive',
            'origin': {
                'isOffice': False,
                'zipcode': 'NW1 6XE',
                'colonyOrDistrict': 'Marylebone',
            },
            'destination': {
                'isOffice': False,
                'zipcode': '31351',
                'colonyOrDistrict': '-',
            },
            'time': '2110-10-20 03:17:52 UTC'
        }]

        expect(response.status).to.equal(falcon.HTTP_OK)
        expect(response.json).to.equal(expected_trips)

    def test_post_trip(self):
        trip = self.VALID_TRIP_PAYLOAD

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_CREATED)
        expect(response.json).to.equal({
            'id': 2,
            'driveOrRide': 'Drive',
            'origin': {
                'isOffice': False,
                'zipcode': 'NW1 6XE',
                'colonyOrDistrict': '-',
            },
            'destination': {
                'isOffice': False,
                'zipcode': 'NW1 6XE',
                'colonyOrDistrict': '-',
            },
            'time': '2016-10-19 20:17:52 UTC'
        })

    def test_post_trip_without_origin(self):
        trip = {}

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_BAD_REQUEST)

    def test_post_trip_without_origin_zipcode(self):
        trip = dict(self.VALID_TRIP_PAYLOAD)
        trip['origin'].pop('zipcode', None)

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_BAD_REQUEST)

    def test_post_trip_without_origin_colony_or_district(self):
        trip = dict(self.VALID_TRIP_PAYLOAD)
        trip['origin'].pop('colonyOrDistrict', None)

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_BAD_REQUEST)

    def test_post_trip_without_destination_zipcode(self):
        trip = dict(self.VALID_TRIP_PAYLOAD)
        trip['destination'].pop('zipcode', None)

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_BAD_REQUEST)

    def test_post_trip_without_destination_colony_or_district(self):
        trip = dict(self.VALID_TRIP_PAYLOAD)
        trip['destination'].pop('colonyOrDistrict', None)

        response = self.simulate_post('/api/trips',
                                      headers={'content-type': 'application/json'},
                                      body=json.dumps(trip))

        expect(response.status).to.equal(falcon.HTTP_BAD_REQUEST)

