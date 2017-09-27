import json

from models.trip import Trip


class TripsResource:
    def on_get(self, req, resp):
        trips = req.db.query(Trip).all()
        resp.body = self._get_serialize_trips(trips)

    def _get_serialize_trips(self, trips):
        return json.dumps([self._get_serialize_trip(trip) for trip in trips])

    def _get_serialize_trip(self, trip):
        return {
            'id': trip.id,
            'driveOrRide': trip.drive_or_ride,
            'origin': {
                'isOffice': False,
                'zipcode': trip.origin.zipcode,
                'colony': trip.origin.colony_or_district,
            },
            'destination': {
                'isOffice': False,
                'zipcode': trip.destination.zipcode,
                'colony': trip.destination.colony_or_district,
            },
            'time': trip.time.strftime('%s')
        }
