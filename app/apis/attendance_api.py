import re
from app.config import api
from flask_restx import Resource 
from app.models.attendance import * 
from flask import jsonify, request
from app.services.rest_model import *
from app.services.attendance_service import *

attendance_model = api.model('attendance', model_to_rest(Attendance()))

# Route for handling the Attendance API
@api.route('/attendance/<int:id>')
class Attendancee(Resource):
    @api.expect(attendance_model)
    def post(self, id):
        args = request.json            
        if check_date(args['check_in'] ,args['check_out'] ):
            save_attendance(id, args)
            return jsonify({"Message" : "Attendance Saved Successfullty"})
        else:
            return jsonify({"Message" : "Please Check Dates"})


    @api.marshal_list_with(attendance_model)
    def get(self,id):
        return get_all_attendance(id)