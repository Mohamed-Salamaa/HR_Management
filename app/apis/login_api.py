from flask import jsonify
from app.config import api
from flask_restx import Resource
from app.models.employees import *
from app.services.users_service import *
from app.services.rest_model import *
from app.services.login_service import *


user_model = api.model('user', model_to_rest(Users()))


# Route for handling the login page logic
@api.route('/login/<int:id>')
class Login(Resource):
    @api.expect(user_model)
    def post(self, id):
        user = get_user_by_id(id)
        if user:
            employee_login(id)
            return 200

@api.route('/logout/<int:id>')
class Logout(Resource):
    @api.expect(user_model)
    def post(self, id):
        user = get_user_by_id(id)
        if user:
            employee_logout(id)
            return 200
