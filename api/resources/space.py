import json
from json.decoder import JSONDecodeError

import falcon

from models import Space


class SpaceResource:
    def on_get(self, req, resp, office_id):
        if not office_id:
            raise falcon.HTTPBadRequest('office_id is required')

        spaces = req.db.query(Space) \
                       .filter(Space.office_id == office_id) \
                       .all()
        resp.json = [self._space_to_json(space) for space in spaces]
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        # TODO validate json paylaod
        data = req.json
        try:
            space = Space(
                office_id=data['office_id'],
                basic_units=json.dumps(data['basic_units']),
                owner_name=data.get('owner_name'),
                owner_id=data.get('owner_id'),
                team=data.get('team'),
                space_type=data.get('space_type')
            )
            req.db.save(space)

            resp.json = self._space_to_json(space)
            resp.status = falcon.HTTP_CREATED
        except (TypeError, JSONDecodeError) as e:
            raise falcon.HTTPBadRequest(e)

    def on_patch(self, req, resp):
        pass

    def on_delete(self, req, resp, space_id):
        if not space_id:
            raise falcon.HTTPBadRequest('space_id is required')

        space_to_be_deleted = req.db.query(Space) \
            .filter(Space.id == space_id) \
            .first()

        req.db.delete(space_to_be_deleted)

        spaces = req.db.query(Space) \
            .filter(Space.office_id == space_to_be_deleted.office_id) \
            .all()

        resp.json = [self._space_to_json(space) for space in spaces]
        resp.status = falcon.HTTP_OK

    def _space_to_json(self, space):
        return {
            'id': space.id,
            'office_id': space.office_id,
            'owner_name': space.owner_name,
            'owner_id': space.owner_id,
            'team': space.team,
            'space_type': space.space_type,
            'basic_units': json.loads(space.basic_units)
        }
