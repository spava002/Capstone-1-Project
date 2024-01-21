from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ry7q9tx98x2ETYojiUX923nJ'
# All database info wil be stored within stocks.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'

db = SQLAlchemy(app)

# Still need to figure out IF stocks db is needed
# And if so, what data is going to be stored here
class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return ""

with app.app_context():
    db.create_all()

# Users database for login feature **WORK IN PROGRESS**
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ""
    
with app.app_context():
    db.create_all()

# Needs to be implemented
# Login page for existing users
# Forms integration needed to collect login information
# Upon login, redirect to /home and update session with user data
@app.route("/", methods=['GET'])
def loginPage():
    return render_template("login.html")

# Needs to be implemented
# Sign in page for new users
# Forms integration needed to collect account creation information
# Upon account creation, redirect to /
@app.route("/signup", methods=['POST'])
def signupPage():
    pass

# Needs to be implemented
# Need to modify POST/GET methods based on use
# Route for main home page
@app.route("/home", methods=['POST', 'GET'])
def homePage():
    pass

# Needs to be implemented
# Logout page for when user is done
# Upon logout, redirect to / and remove user data from session
@app.route("/logout")
def logoutUser():
    pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")