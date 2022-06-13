from flask import Flask 
from flask_restx import Api , Resource 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initilaize Flask App
app = Flask(__name__)

api = Api(app)

# Set Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://salama:salama@localhost:5432/HR_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize Database using SQLAlchemy
db = SQLAlchemy(app)
#initialize Migration Object

migrate = Migrate(app, db)
from apis import *
from models import *

if __name__ == "__main__":
    app.run(debug=True)
