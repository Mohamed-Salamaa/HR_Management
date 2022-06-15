from app.config import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.services.model_util import * 

class Users(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    user_name = db.Column (db.String(200) , nullable = False)
    password  = db.Column (db.String(200) , nullable = False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)


    #model to dict function
    def to_dict(self):
        return model_to_dict(self)

    #model form dict function
    def to_model(self, employee_dict):
        model_from_dict(self , **employee_dict)
    
    def get_columns_name(self):
        column_list = self.to_dict(self).keys()
        return column_list