from app.config import api
from flask_restx import Resource 
from app.models.attendance import * 
from app.services.rest_model import *
from app.services.attendance_service import *

attendance_model = api.model('attendance', model_to_rest(Attendance()))

# Route for handling the Attendance API
@api.route('/attendance/<int:id>')
class Attendancee(Resource):
    @api.marshal_list_with(attendance_model)
    def get(self,id):
        return get_employee_attendance(id)

# Route for handling the Check In API
@api.route('/checkin/<int:id>')
class CheckIn(Resource):
    def post(self , id):
        return check_in(id )

# Route for handling the Check Out API
@api.route('/checkout/<int:id>')
class CheckOut(Resource):
    def post(self , id):
        return check_out(id)