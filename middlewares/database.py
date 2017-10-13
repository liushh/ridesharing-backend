class DatabaseMiddleware:
    def __init__(self, db):
        self.db = db

    def process_resource(self, req, resp, resource, params):
        print('DatabaseMiddleware process_resource start')
        req.db = self.db.make_session()
        print('DatabaseMiddleware process_resource done')

    def process_response(self, req, resp, resource, req_succeeded):
        print('DatabaseMiddleware process_response start')
        if hasattr(req, 'db'):
            req.db.close()
        print('DatabaseMiddleware process_response done')
