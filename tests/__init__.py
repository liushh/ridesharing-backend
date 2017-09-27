# flake8: noqa
from falcon import testing
from datetime import datetime

from config import Test
from api.server import App


class TestCase(testing.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.app = App(Test)
        db = self.app.get_database()
        db.create_database()

        self.make_a_trip()

    def tearDown(self):
        db = self.app.get_database()
        db.delete_database()


    def make_a_trip(self):
        from models import Trip, User, Origin, Destination

        session = self.get_session()

        user = User(username='liusha@wizeline.com',
                    email='liusha@wizeline.com',
                    phone='123456789',
                    auth0_id='123')
        session.save(user)

        origin = Origin(street='Baker St',
                        street_number='221B',
                        colony_or_district='Marylebone',
                        city='London',
                        state='Marylebone',
                        country='UK',
                        zipcode='NW1 6XE')
        session.save(origin)

        destination = Destination(street='Wallaby Way',
                                  street_number='42',
                                  colony_or_district='-',
                                  city='Sydney',
                                  state='New South Wales',
                                  country='Australia',
                                  zipcode='31351')
        session.save(destination)

        trip = Trip(drive_or_ride='Drive',
                    time=datetime(1992, 9, 4),
                    origin=origin,
                    destination=destination,
                    user=user)
        session.save(trip)

    def get_session(self):
        if not hasattr(self, '_session'):
            db = self.app.get_database()
            self._session = db.make_session()

        return self._session
