from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__, template_folder='UI')
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret Key
app.config['SECRET_KEY'] = "secretKey" 

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
 


# Models
class Profile(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    age = db.Column(db.Integer, nullable=False)
 
    def __init__(self, name, first_name, last_name, age):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"
    
    def test_connection(self):
        with app.app_context():
            pass
 
# Create a form class
class NamerForm(FlaskForm):
    name = StringField("What is Your Name")
    submit = SubmitField("Submit")



# function to render index page
@app.route('/')
def index():
    return render_template('homepage.html', msg='Hello')
 
if __name__ == '__main__':
    app.run()