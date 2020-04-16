from . import db
from flask import datetime
#from werkzeug.security import generate_password_hash

"""def format_date_joined(year, month, day):
    now = datetime.datetime.now() # today's date
    date_joined = datetime.date(year, month, day) # a specific date 
    answer = "Joined " + date_joined.strftime("%B, %Y")
    return answer"""
    
class User(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    #profilepic = db.Column(db.String(80)) #unsure
    #date=db.format_date_joines(2020,3,15)
    date=db.DateTimeField(default=datetime.now) #current date
    
    #def __init__(self, first_name, last_name, username, password):
    def __init__(self, first_name, last_name, gender, email, location, biography, date): #add profilepic?
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        #self.profilepic = profilepic
        self.date = date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.firstname, self.last_name
