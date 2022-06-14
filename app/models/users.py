from app.config import db
from app.services.model_util import *


class Users(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    user_name = db.Column (db.String(200) , nullable = False)
    password  = db.Column (db.String(200) , nullable = False)
    email = db.Column (db.String(200) , nullable = False)


    #model to dict function
    def to_dict(self):
        return model_to_dict(self)

    #model form dict function
    def to_model(self, user_dict):
        model_from_dict(self , **user_dict)
    
    def get_columns_name(self):
        column_list = self.to_dict(self).keys()
        return column_list
