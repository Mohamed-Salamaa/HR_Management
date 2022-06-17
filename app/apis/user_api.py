from app.config import api
from flask_restx import Resource 
from app.models.users import * 
from flask import request
from app.services.rest_model import *
from app.services.users_service import *

user_model = api.model('user', {
  "user_name": fields.String,
  "password": fields.String,
  "employee_id": fields.Integer
})

# Route for handling the User API
@api.route('/users')
class User(Resource):
    @api.expect(user_model)
    def post(self):
        args = request.json
        save_user(args)
        return 200