import json

from models.trip import Trip


class TripsResource:
    def on_get(self, req, resp):
        trip = req.db.query(Trip).first()
        resp.body = json.dumps(self.get_serialize_trip(trip))

    def get_serialize_trip(self, trip):
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
