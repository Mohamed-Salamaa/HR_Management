import re
from app.config import api
from flask_restx import Resource 
from app.models.attendance import * 
from flask import request
from app.services.rest_model import *
from app.services.attendance_service import *

attendance_model = api.model('attendance', model_to_rest(Attendance()))

# Route for handling the Attendance API
@api.route('/attendance/<int:id>')
class Attendancee(Resource):
    # @api.marshal_list_with(attendance_model)
    @api.expect(attendance_model)
    def post(self, id):
        args = request.json
        save_attendance(id, args)
        return 200


    @api.marshal_list_with(attendance_model)
    def get(self,id):
        return get_all_attendance(id)