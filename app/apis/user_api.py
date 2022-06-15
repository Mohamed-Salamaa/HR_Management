from app.config import api
from flask_restx import Resource 
from app.models.users import * 
from flask import request
from app.services.rest_model import *
from app.services.users_service import *

user_model = api.model('user', model_to_rest(Users()))


@api.route('/users')
class User(Resource):
    @api.expect(user_model)
    def post(self):
        args = request.json
        save_user(args)
        return 200


    @api.marshal_list_with(user_model)
    def get(self):
        users_list = get_all_users()
        return users_list
