import json
from app.config import app
from flask import jsonify, render_template,  request , session 
from app.models.employees import *

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])

def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        search_query = db.session.query(Employee)
        account = search_query.filter(Employee.user_name == username , Employee.password == password).first()
        if account:
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.user_name
            msg = 'Logged in successfully !'
            return jsonify ({"message" : "Logged in successfully!!"})
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)