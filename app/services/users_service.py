from app.config import db
from app.models.users import *


def save_user(user_dict):
    user = Users()
    user.to_model(user_dict)
    db.session.add(user)
    db.session.commit()

def get_user_by_id(id):
    search_query = db.session.query(Users)
    user = search_query.filter(Users.employee_id == id).first()
    return user
