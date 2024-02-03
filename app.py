from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from login_form import login
from signup_form import signup
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

# Landing page with login/sign-up fields
@app.route("/", methods=['POST', 'GET'])
def loginPage():
    login_form = login()
    signup_form = signup()
    return render_template("login.html", login_form=login_form, signup_form=signup_form)


# Login functionality for existing users
# Upon login, redirect to /home and update session with username
@app.route("/login", methods=['POST', 'GET'])
def loginUser():
        login_form = login()
        signup_form = signup()
        if login_form.validate_on_submit():
            print("Login submitted.")
            username = login_form.username.data
            password = login_form.username.data
            currentUser = Users.query.filter_by(username=username).first()
            if currentUser and currentUser.password == password:
                session['current_user'] = username
                return redirect(url_for("homePage"))
            else:
                flash("Invalid username or password. Try again.", "login_error")
        return render_template("login.html", login_form=login_form, signup_form=signup_form)


# Sign in functionality for new users
# Upon account creation, redirect to /home and update session with username
@app.route("/sign-up", methods=['POST', 'GET'])
def signupUser():
    login_form = login()
    signup_form = signup()
    if signup_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.username.data
        newUser = Users.query.filter_by(username=username).first()
        # User exists in database
        if newUser:
            flash("Username taken. Try again.", "signup_error")
        # User doesn't exist in database
        else:
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['current_user'] = username
            return redirect(url_for("homePage"))
    return render_template("login.html", login_form=login_form, signup_form=signup_form)


# Route for main home page
@app.route("/home", methods=['POST', 'GET'])
def homePage():
    current_user = session.get('current_user')
    return render_template("home.html", current_user=current_user)

# Needs to be implemented
# Logout page for when user is done
# Upon logout, redirect to / and remove user data from session
@app.route("/logout")
def logoutUser():
    pass

@app.route("/db")
def usersDatabase():
    users_data = Users.query.all()
    return render_template('database.html', users_data=users_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")