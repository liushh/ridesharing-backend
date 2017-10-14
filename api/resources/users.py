import falcon


class UsersResource:
    def on_get(self, req, resp):
        print('GET USER!!!!!!!!!!!!!!!!!!!!!')
        print('req.current_user[serialized_data] = ', req.current_user['serialized_data'])
        resp.json = req.current_user['serialized_data']
        resp.status = falcon.HTTP_OK
