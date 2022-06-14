from app.config import db
from app.models.users import *



def add_user(users_dict):
    user = Users()
    user.to_model(users_dict)
    db.session.add(user)
    db.session.commit()

def get_all_users():
    search_query = db.session.query(Users)
    users_list = search_query.all()
    return users_list
