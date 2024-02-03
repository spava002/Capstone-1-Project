from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from loginForm import login
from signupForm import signUp
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
    loginForm = login()
    signupForm = signUp()
    return render_template("login.html", loginForm=loginForm, signupForm=signupForm)


# Login functionality for existing users
# Upon login, redirect to /home and update session with username
@app.route("/login", methods=['POST', 'GET'])
def loginUser():
        loginForm = login()
        signupForm = signUp()
        if loginForm.validate_on_submit():
            print("Login submitted.")
            username = loginForm.username.data
            password = loginForm.username.data
            currentUser = Users.query.filter_by(username=username).first()
            if currentUser and currentUser.password == password:
                session['currentUser'] = username
                return redirect(url_for("homePage"))
            else:
                flash("Invalid username or password. Try again.", "loginError")
        return render_template("login.html", loginForm=loginForm, signupForm=signupForm)


# Sign in functionality for new users
# Upon account creation, redirect to /home and update session with username
@app.route("/sign-up", methods=['POST', 'GET'])
def signupUser():
    loginForm = login()
    signupForm = signUp()
    if signupForm.validate_on_submit():
        print("Sign up submitted.")
        username = loginForm.username.data
        password = loginForm.username.data
        newUser = Users.query.filter_by(username=username).first()
        # User exists in database
        if newUser:
            print("A user already exists.")
            flash("Username taken. Try again.", "signupError")
        # User doesn't exist in database
        else:
            print("User created.")
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['currentUser'] = username
            return redirect(url_for("homePage"))
    return render_template("login.html", loginForm=loginForm, signupForm=signupForm)


# Route for main home page
@app.route("/home", methods=['POST', 'GET'])
def homePage():
    current_user = session.get('currentUser')
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