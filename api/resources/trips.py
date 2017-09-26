import falcon

from models.trip import Trip


class TripsResource:
    def on_get(self, req, resp):
        trip = req.db.query(Trip).first()

        resp.body = (self.get_serialize_trip(trip))

    def get_serialize_trip(self, trip):
        return {
            'uuid': trip.uuid,
            'driveOrRide': trip.drive_or_ride,
            'origin': {
                'isOffice': False,
                'zipcode': trip.origin.zipcode,
                'colony': trip.origin.colony,
            },
            'destination': {
                'isOffice': False,
                'zipcode': trip.destination.zipcode,
                'colony': trip.destination.colony,
            },
            'time': trip.time
        }
