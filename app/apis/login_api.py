from flask import jsonify
from app.config import api
from flask_restx import Resource
from app.models.employees import *
from app.services.users_service import *
from app.services.rest_model import *
from app.services.login_service import *


user_model = api.model('user', model_to_rest(Users()))


# Route for handling the login API
@api.route('/login/<int:id>')
class Login(Resource):
    @api.expect(user_model)
    def post(self, id):
        user = get_user_by_id(id)
        if user:
           Result =  employee_login(id)
        return Result

@api.route('/logout/<int:id>')
class Logout(Resource):
    def post(self, id):
        user = get_user_by_id(id)
        if user:
            Result = employee_logout(id)
        return Result