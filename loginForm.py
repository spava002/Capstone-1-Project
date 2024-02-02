from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class login(FlaskForm):
    # Required parameters to login
    username = StringField('Username: ', validators=[DataRequired(), Length(min=3, max=50, message='Invalid username. Must be between 3-20 characters.')], render_kw={"autocomplete": "off"})
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=3, max=50)])
    # Submits data to backend
    submit = SubmitField('Login')