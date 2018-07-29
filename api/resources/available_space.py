import json
from json.decoder import JSONDecodeError

import falcon

from models import Space


class AvailableSpaceResource:
    def on_get(self, req, resp, office_id):
        if not office_id:
            raise falcon.HTTPBadRequest('office_id is required')

        employee_desk_count = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .filter(Space.space_type == 'Employee Desk') \
                       .count()
        available_employee_desk_count = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .filter(Space.space_type == 'Employee Desk') \
                       .filter(Space.owner_name == '') \
                       .count()

        visitor_desk_count = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .filter(Space.space_type == 'Visitor Desk') \
                       .count()
        available_visitor_desk_count = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .filter(Space.space_type == 'Visitor Desk') \
                       .filter(Space.owner_name == '') \
                       .count()

        empty_desk_count = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .filter(Space.space_type == 'Empty Desk') \
                       .count()
        resp.json = {
            'employee_desk': {
                'available': available_employee_desk_count,
                'total': employee_desk_count
            },
            'visitor_desk': {
                'available': available_visitor_desk_count,
                'total': visitor_desk_count
            },
            'empty_desk': {
                'available': empty_desk_count,
                'total': empty_desk_count
            }
        }
        resp.status = falcon.HTTP_OK