"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
import psycopg2
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserProfile
#import datetime
from models import User
from app import app, db
from werkzeug.utils import secure_filename
###
# Routing for your application.
###
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the website's about page."""
    #return render_template('about.html', name="Tiffany Garrick")
    return render_template('about.html')

def connect_db():
 return psycopg2.connect(host="localhost",database="project", user="postgres", password="@Poogiebear123") 

@app.route('/profile', methods=['GET','POST'])
def profile():
    """Render the website's adding profile page."""
    User = UserProfile()
    if request.method == 'POST':
        if User.validate_on_submit():
            db = connect_db()
            cur = db.cursor()
            firstname = User.firstname.data
            lastname = User.lastname.data
            gender = User.gender.data
            email = User.email.data
            location = User.location.data
            biography = User.biography.data
            profilepic = User.profilepic.data
            date=User.date.data
            
            filename = secure_filename(profilepic.filename)
            profilepic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            cur.execute('insert into user_profiles (firstname, lastname, gender, email, location, biography, date)values (%s, %s, %s, %s, %s, %s %s)', (request.form['firstname'],request.form['lastname'],request.form['gender'],request.form['email'],request.form['location'],request.form['biography'], request.form['date']))
            db.commit()
            flash('The profile was succesfully added', 'success')
            return redirect(url_for('profiles'), filename=filename, form=User)
        flash_errors(User)
    
    return render_template('profile.html')

@app.route('/profiles')
def profiles():
    """Render the website's profiles list page."""
    db = connect_db()
    cur = db.cursor()
    cur.execute('select firstname, lastname, gender, email, location, biography, date from user_profiles order by id desc')
    users=cur.fetchall()
    return render_template('profiles.html', users=users)

@app.route('/profile/<userid>')
def profile_specific(userid):
#Render the website's specific profile page based on user id
    form=UserProfile()
    if(User.query.get(int(userid))):
        date=User.query.get(form.date.data)
        firstname=User.query.get(form.first_name.data)
        lastname=User.query.get(form.last_name.data)
        #gender=User.query.get(form.gender.data)
        email=User.query.get(form.email.data)
        location=User.query.get(form.location.data)
        biography=User.query.get(form.biography.data)
        return render_template("user_specific.html", date=date,firstname=firstname,lastname=lastname,
            email=email,location=location,biography=biography)
    else:
        #return error page
        return render_template ('404.html')

# Flash errors from the form if validation fails with Flask-WTF
# http://flask.pocoo.org/snippets/12/
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'danger')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
