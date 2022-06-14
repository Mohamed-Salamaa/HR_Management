from app.config import db
from app.models.attendance import *

def save_attendance(id ,attendance_dict):
    attendance = Attendance()
    attendance.to_model(attendance_dict)
    db.session.add(attendance)
    db.session.commit()


def get_all_attendance(id):
    search_query = db.session.query(Attendance)
    attendance_list = search_query.filter_by(id == id).all()
    return attendance_list