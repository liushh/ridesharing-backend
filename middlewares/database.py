class DatabaseMiddleware:
    def __init__(self, db):
        self.db = db

    def process_resource(self, req, resp, resource, params):
        req.db = self.db.make_session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(req, 'db'):
            req.db.close()
