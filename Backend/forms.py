from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length


class RegistrationForm(FlaskForm):
    Email = StringField('Email',validators=[DataRequired(),Email(message='please entre an valid Email')])
    Password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=15)])
    Submit = SubmitField ('Regiseter')

class LoginForm (FlaskForm):
    Email = StringField('Email',validators=[DataRequired(),Email()])
    Password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=15)])
    Submit = SubmitField ('Login')