from datetime import datetime
import json

import falcon
from sure import expect

from tests import TestCase


class TestTrips(TestCase):
    # def test_get_all_trips(self):
    #     response = self.simulate_get('/api/trips')
    #     expected_trips = [{
    #         'id': 1,
    #         'driveOrRide': 'Drive',
    #         'origin': {
    #             'isOffice': False,
    #             'zipcode': 'NW1 6XE',
    #             'colony': 'Marylebone',
    #         },
    #         'destination': {
    #             'isOffice': False,
    #             'zipcode': '31351',
    #             'colony': '-',
    #         },
    #         'time': datetime(1992, 9, 4).strftime('%s')
    #     }]

    #     expect(response.status).to.equal(falcon.HTTP_OK)
    #     expect(response.json).to.equal(expected_trips)

    def test_get_all_trips_return_empty_array(self):
        response = self.simulate_get('/api/trips')
        expect(response.status).to.equal(falcon.HTTP_OK)
        expect(response.json).to.equal([])   

    def test_post_trip(self):
        trip = {
            'email': 'liusha@wizeline.com',
            'driveOrRide': 'Drive',
            'hoursAndMinutes': '12:09',
            'day': '04',
            'month': '05',
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
            'time': datetime.now().replace(minute=9, hour=12, month=5, day=4).strftime('%s')
        })
