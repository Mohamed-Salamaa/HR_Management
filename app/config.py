from flask import Flask 
from flask_restx import Api  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initilaize Flask App
app = Flask(__name__)

api = Api(app)

# Set Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://salama:salama@localhost:5434/HR_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Set Secret Key into Session
app.secret_key =os.urandom(24)

#initialize Database using SQLAlchemy
db = SQLAlchemy(app)
#initialize Migration Object

migrate = Migrate(app, db)