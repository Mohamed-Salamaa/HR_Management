from app.config import db
from datetime import datetime
from flask import jsonify
from app.models.attendance import *
from app.models.employees import *


def get_employee_attendance(id):
    employee_search_query = db.session.query(Employee)
    employee = employee_search_query.get(id)
    if employee:
        if employee.check_login == True:
            attendance_search_query = db.session.query(Attendance)
            attendance_list = attendance_search_query.filter(Attendance.employee_id == id).all()
            return attendance_list


def check_date(id):
    attendance_search_query = db.session.query(Attendance)
    attendance_record = attendance_search_query.filter(Attendance.check_in != None).order_by(Attendance.employee_id.desc()).first()
    if attendance_record.check_in <= datetime.now():
        return True
    else:
        return False


def check_in(id):
    msg = ''
    employee_search_query = db.session.query(Employee)
    employee = employee_search_query.get(id)
    if employee:
        if employee.check_login == True and employee.checked_in == False:
            employee.checked_in = True
            db.session.add(employee)
            attendance = Attendance()
            attendance.employee_id = id
            attendance.check_in = datetime.now()
            db.session.add(attendance)
            db.session.commit()
            msg = 'Checked in Success'
            return jsonify({"Message" : msg})
        else:
            msg = 'Error has occured'
            return jsonify({"Error" : msg})
    else:
        return jsonify({"Error" : "There is no Employee with this ID"})
    


def check_out(id):
    if check_date(id):
        msg = ''
        employee_search_query = db.session.query(Employee)
        employee = employee_search_query.get(id)
        if employee:
            if employee.check_login == True and employee.checked_in == True:
                employee.checked_in = False
                db.session.add(employee)
                attendance= Attendance()
                attendance_search_query = db.session.query(Attendance)
                attendance = attendance_search_query.filter(Attendance.check_out == None).order_by(Attendance.employee_id.desc()).first()
                attendance.check_out =  datetime.now()
                db.session.add(attendance)
                db.session.commit()
                msg = 'Checked out Success'
                return jsonify({"Message" : msg})
            else:
                msg = 'Error has occured'
                return jsonify({"Error" : msg})
        else:
            return jsonify({"Error" : "There is no Employee with this ID"})
    else:
            return jsonify({"Error" : "Check out Date Must be Bigger Than Check in Date"})
