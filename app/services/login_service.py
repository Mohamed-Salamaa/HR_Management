from app.config import db
from app.models import *
from flask import jsonify

def employee_login(id):
    employee = Employee()
    search_query = db.session.query(Employee)
    employee = search_query.get(id)
    if employee.check_login == False:
        employee.check_login = True
        db.session.add(employee)
        db.session.commit()
        msg = 'Login Successfully'
    else:
        msg = 'You are already Login'
    return jsonify ({"Message" : msg})

def employee_logout(id):
    msg = ''
    employee = Employee()
    search_query = db.session.query(Employee)
    employee = search_query.get(id)
    if employee.check_login == True:
        employee.check_login = False
        db.session.add(employee)
        db.session.commit()
        msg = 'Successfully Logout'
    else:
        msg = 'You are not Login'
    return jsonify ({"Message" : msg})