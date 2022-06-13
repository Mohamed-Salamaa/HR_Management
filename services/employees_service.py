from run import db
from models.employees import *



def save_employee(employee_dict):
    employee = Employee()
    employee.to_model(employee_dict)
    db.session.add(employee)
    db.session.commit()

def get_all_employees():
    search_query = db.session.query(Employee)
    employees = search_query.all()
    return employees
