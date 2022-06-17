from email.policy import default
from  app.config import db
from app.services.model_util import * 
from sqlalchemy.orm import  relationship

class Employee(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    employee_name = db.Column (db.String(200) , nullable = False)
    check_login = db.Column(db.Boolean , default=False )
    checked_in = db.Column(db.Boolean, default=False)
    user = db.relationship('Users', backref='Users', lazy=True, uselist=False)


    #model to dict function
    def to_dict(self):
        return model_to_dict(self)

    #model form dict function
    def to_model(self, employee_dict):
        model_from_dict(self , **employee_dict)
    
    def get_columns_name(self):
        column_list = self.to_dict(self).keys()
        return column_list