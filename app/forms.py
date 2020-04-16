from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, SubmitField, SelectField, TextAreaField
from wtforms import StringField, Length, SubmitField
from wtforms.validators import DataRequired, Email

class UserProfile(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(message='A username is required'),Length(min=2, max=25)])
    lastname = StringField('Last Name', validators=[DataRequired(message='A username is required'),Length(min=2, max=25)])
    gender = SelectField('Gender', choices = [('Male', 'Male'),('Female', 'Female')])
    email = StringField('E-mail', validators=[Length(min=6, max=35), Email(message='An email address is required')])
    location = StringField('Location', validators=[DataRequired(message='A message is required')])
    biography = TextAreaField('Biography', validators=[DataRequired(message='A message is required')])
    profilepic = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    submit=SubmitField('Add Profile')
    