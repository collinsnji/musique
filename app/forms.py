from flask_wtf import FlaskForm  # Flask wrapper
from wtforms import StringField, PasswordField, BooleanField, SubmitField   # Python WTF elements
from wtforms.validators import DataRequired


class Login(FlaskForm):
    username = StringField('Username', render_kw={"placeholder":"Enter your username"}, validators=[DataRequired()])
    password = PasswordField('Password',render_kw={"placeholder":"Enter your password"}, validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignUp(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    cancel_button = SubmitField()
