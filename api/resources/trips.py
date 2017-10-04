import json
from datetime import datetime
from dateutil import parser

import falcon

from models import Trip, User, Origin, Destination


class TripsResource:
    REQUIRED_REQUEST_ATTRS = [
        'email',
        'driveOrRide',
        'time',
        'origin',
        'destination'
    ]

    def on_post(self, req, resp):
        print('POST!!!!!!!!!!!!!!!!!!')
        data = req.json
        if not self._is_valid_request_payload(data):
            raise falcon.HTTPBadRequest()

        try:
            origin = self._get_location(Origin, data['origin'])
            req.db.save(origin)
        except KeyError:
            raise falcon.HTTPBadRequest('Invalid origin payload')

        try:
            destination = self._get_location(Destination, data['destination'])
            req.db.save(destination)
        except KeyError:
            raise falcon.HTTPBadRequest('Invalid destination payload')

        trip = Trip(drive_or_ride=data['driveOrRide'],
                    origin=origin,
                    destination=destination,
                    user=req.current_user,
                    time=parser.parse(data['time']))  # data['time'] example: 2016-10-19T20:17:52.2891902Z
        req.db.save(trip)

        resp.json = self._get_serialize_trip(trip)
        resp.status = falcon.HTTP_CREATED

    def _is_valid_request_payload(self, data):
        keys = data.keys()
        if keys == {}:
            return False
        for attr in self.REQUIRED_REQUEST_ATTRS:
            if attr not in keys:
                return False
        return True

    def _get_current_user(self, query, email):
        user = query(User) \
            .filter(User.email == email).first()
        print('user = ', user)
        return user

    def _get_location(self, data_model_klass, data):
        return data_model_klass(
            street=self._get_location_attr(data, 'street'),
            street_number=self._get_location_attr(data, 'streetNumber'),
            colony_or_district=data['colonyOrDistrict'],
            city=self._get_location_attr(data, 'city'),
            state=self._get_location_attr(data, 'state'),
            country=self._get_location_attr(data, 'country'),
            zipcode=data['zipcode'])

    def _get_location_attr(self, location_data, attr):
        return location_data.get(attr) or ''

    def on_get(self, req, resp):
        print('GET!!!!!!!!!!!!!!!!!!!!!')
        trips = req.db.query(Trip).filter(Trip.time > datetime.now())
        resp.body = self._get_serialize_trips(trips)
        resp.status = falcon.HTTP_OK

    def _get_serialize_trips(self, trips):
        return json.dumps([self._get_serialize_trip(trip) for trip in trips])

    def _get_serialize_trip(self, trip):
        return {
            'id': trip.id,
            'email': trip.user.email,
            'name': trip.user.username,
            'phone': trip.user.phone,
            'driveOrRide': trip.drive_or_ride,
            'origin': {
                'isOffice': False,
                'zipcode': trip.origin.zipcode,
                'colonyOrDistrict': trip.origin.colony_or_district,
            },
            'destination': {
                'isOffice': False,
                'zipcode': trip.destination.zipcode,
                'colonyOrDistrict': trip.destination.colony_or_district,
            },
            'time': trip.time.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
