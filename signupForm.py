from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


# Checks for valid passwords
# Valid includes: a digit, uppercase, and longer than 8 characters
def validatePassword(form, field):
    password = field.data
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        raise ValidationError("Password must be 8 characters minimum, include an uppercase character, and a number.")


# Checks if 'password' is same as 'confirm password'
def confirmPassword(form, field):
    if form.password.data != field.data:
        raise ValidationError("Passwords do not match!")


class signUp(FlaskForm):
    # Required parameters to sign up
    username = StringField('Username: ', validators=[DataRequired(), Length(min=3, max=50, message='Invalid username. Must be between 3-20 characters.')], render_kw={"autocomplete": "off"})
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=3, max=50), validatePassword])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), Length(min=3, max=50), confirmPassword])
    # Submits data to backend
    submit = SubmitField('Sign Up')