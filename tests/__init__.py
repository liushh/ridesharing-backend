# flake8: noqa
from falcon import testing
from datetime import datetime

from config import Test
from api.server import App


class TestCase(testing.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.app = App(Test)
        self.make_a_trip()


    def make_a_trip(self):
        from models import Trip, User, Location

        session = self.get_session()

        user = User(username='liusha@wizeline.com',
                    email='liusha@wizeline.com',
                    phone='123456789',
                    auth0_id='123')

        session.save(user)

        origin = Location(street='Baker St',
                            streetNumber='221B',
                            colony_or_district='221B',
                            city='London',
                            state='Marylebone',
                            country='UK',
                            zipcode='NW1 6XE')
        session.save(origin)

        destination = Location(street='Baker St',
                            streetNumber='221B',
                            colony_or_district='221B',
                            city='London',
                            state='Marylebone',
                            country='UK',
                            zipcode='NW1 6XE')
        session.save(origin)

        trip = Trip(drive_or_ride='Drive',
                    time=datetime.now(),
                    origin=origin,
                    destination=destination,
                    user=user)
        session.save(trip)

    def get_session(self):
        if not hasattr(self, '_session'):
            db = self.app.get_database()
            self._session = db.make_session()

        return self._session
