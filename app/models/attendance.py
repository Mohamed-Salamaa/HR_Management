from app.config import db
from app.services.model_util import * 

class Attendance(db.Model):
    
    id = db.Column (db.Integer , primary_key = True , autoincrement = True, nullable = False)
    check_in = db.Column (db.DateTime, nullable = True)
    check_out = db.Column (db.DateTime ,nullable = True)

    employee_id = db.Column(db.Integer , db.ForeignKey('employee.id') , nullable = False)
    employee = db.relationship('Employee', backref='Attendance')

    #model to dict function
    def to_dict(self):
        return model_to_dict(self)

    #model form dict function
    def to_model(self, attendance_dict):
        model_from_dict(self , **attendance_dict)
    
    def get_columns_name(self):
        column_list = self.to_dict(self).keys()
        return column_list