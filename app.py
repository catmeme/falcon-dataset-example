# sample.py
import falcon
import json
import dataset

db = dataset.connect()
users_table = db['user']


class UsersResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        users = []
                     
        for user in db['user']:
            users.append(user)

        resp.body = json.dumps(users)

    def on_post(self, req, resp):
        """Handles POST requests"""
        users_table.insert(req.params)

    def on_put(self, req, resp):
        """Handles PUT requests"""
        data = req.params
        users_table.update(data, ['id'])

    def on_delete(self, req, resp):
        """Handles DELETE requests"""
        data = req.params
        users_table.delete(id=data['id'])


api = falcon.API()
api.add_route('/users', UsersResource())
