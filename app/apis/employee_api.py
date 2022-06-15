from app.config import api
from flask_restx import Resource 
from app.models.employees import * 
from flask import request
from app.services.rest_model import *
from app.services.employees_service import *

employee_model = api.model('employee', model_to_rest(Employee()))

# Route for handling the Employee API
@api.route('/employees')
class Employees(Resource):
    @api.expect(employee_model)
    def post(self):
        args = request.json
        save_employee(args)
        return 200


    @api.marshal_list_with(employee_model)
    def get(self):
        employees_list = get_all_employees()
        return employees_list