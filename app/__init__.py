from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost/database"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:@Poogiebear@localhost/project"
app.config['SQLALCHEMY_DATABASE_URL'] = "postgres://gojtqlllhhakzr:f25325e71b9e5c31926ab00a7d9f97c3a37041deb26fc878298b0b6f36b80907@ec2-54-157-78-113.compute-1.amazonaws.com:5432/dbueclfqep5ei"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  #suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models
