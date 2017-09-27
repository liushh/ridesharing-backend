import json
from datetime import datetime

import falcon

from models import Trip, User, Origin, Destination


class TripsResource:
    def on_post(self, req, resp):
        data = req.json

        origin = self._get_location(Origin, data['origin'])
        req.db.save(origin)

        destination = self._get_location(Destination, data['destination'])
        req.db.save(destination)

        trip = Trip(drive_or_ride='Drive',
                    origin=origin,
                    destination=destination,
                    user=self._get_current_user(req.db.query, data),
                    time=self._get_trip_time(data))
        req.db.save(trip)

        resp.json = self._get_serialize_trip(trip)
        resp.status = falcon.HTTP_CREATED

    def _get_current_user(self, query, data):
        user = query(User) \
            .filter(User.email == data['email']).first()
        return user

    def _get_location(self, data_model_klass, data):
        return data_model_klass(
            street=self._get_location_attr(data, 'street'),
            street_number=self._get_location_attr(data, 'streetNumber'),
            colony_or_district=self._get_location_attr(data, 'colonyOrDistrict'),
            city=self._get_location_attr(data, 'city'),
            state=self._get_location_attr(data, 'state'),
            country=self._get_location_attr(data, 'country'),
            zipcode=self._get_location_attr(data, 'zipcode'))

    def _get_location_attr(self, location_data, attr):
        return location_data.get(attr) or ''

    def _get_trip_time(self, data):
        minute = self._get_minute(data['hoursAndMinutes'])
        hour = self._get_hour(data['hoursAndMinutes'])
        month = data['month'].lstrip('0')
        day = data['day'].lstrip('0')
        return datetime.now().replace(minute=int(minute),
                                      hour=int(hour),
                                      month=int(month),
                                      day=int(day))

    def _get_minute(self, hoursAndMinutes):
        minute = hoursAndMinutes.split(':')[1]
        return minute.lstrip('0')

    def _get_hour(self, hoursAndMinutes):
        hour = hoursAndMinutes.split(':')[0]
        return hour.lstrip('0')


    def on_get(self, req, resp):
        trips = req.db.query(Trip).filter(Trip.time > datetime.now())
        resp.body = self._get_serialize_trips(trips)
        resp.status = falcon.HTTP_OK

    def _get_serialize_trips(self, trips):
        return json.dumps([self._get_serialize_trip(trip) for trip in trips])

    def _get_serialize_trip(self, trip):
        return {
            'id': trip.id,
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
            'time': trip.time.strftime('%s')
        }
