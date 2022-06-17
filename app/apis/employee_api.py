from app.config import api
from flask_restx import Resource 
from app.models.employees import * 
from flask import request
from app.services.rest_model import *
from app.services.employees_service import *

employee_model = api.model('employee', {
    'employee_name' : fields.String
})

# Route for handling the Employee API
@api.route('/register')
class Employees(Resource):
    @api.expect(employee_model)
    def post(self):
        args = request.json
        save_employee(args)
        return 200