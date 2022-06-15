from app.config import db
from app.models.attendance import *
from app.models.employees import *


def save_attendance(id ,attendance_dict):
    employee_search_query = db.session.query(Employee)
    employee = employee_search_query.get(id)
    if employee:
        if employee.check_login == True:
            attendance = Attendance()
            attendance.to_model(attendance_dict)
            db.session.add(attendance)
            db.session.commit()


def get_all_attendance(id):
    employee_search_query = db.session.query(Employee)
    employee = employee_search_query.get(id)
    if employee:
        if employee.check_login == True:
            attendance_search_query = db.session.query(Attendance)
            attendance_list = attendance_search_query.filter(Attendance.employee_id == id).all()
            print(attendance_list)
            return attendance_list