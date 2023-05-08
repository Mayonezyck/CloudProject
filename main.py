from flask import Flask, request, redirect, flash, url_for, session
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__, template_folder='UI',static_folder='staticfiles')
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret Key
app.config['SECRET_KEY'] = "secretKey" 
#upload folder
app.config['UPLOAD_FOLDER'] = os.path.join('staticfiles', 'uploads')
#API ip
app.config['API_IP'] = '104.154.96.207'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
# Models
class Profile(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    age = db.Column(db.Integer, nullable=False)
 
    def __init__(self, first_name, last_name, age):
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
 
@app.route('/show')
def show_all():
   return render_template('show_all.html', users = Profile.query.all() )

@app.route('/use')
def use_serv():
    return render_template('usage.html')

@app.route('/pic')
def uploadFile():
    return render_template('index_upload.html')

@app.route('/pic',  methods=("POST", "GET"))
def showFile():
    if request.method == 'POST':
        # Upload file flask
        uploaded_img = request.files['uploaded-file']
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
 
        return render_template('image_upload_show.html')

@app.route('/', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['fname'] or not request.form['lname'] or not request.form['age']:
         flash('Please enter all the fields', 'error')
      else:
         user = Profile(request.form['fname'], request.form['lname'], request.form['age'])
         
         db.session.add(user)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('use_serv'))
   return render_template('new.html')

@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    img_file_path = session.get('uploaded_img_file_path', None)
    print(img_file_path)
    api_path = 'https://' + app.config['API_IP'] + ':5000/model/predict?image=' + img_file_path
    headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    #'Content-Type': 'multipart/form-data',
    }

    files = {'image': open(img_file_path, 'rb')}

    modelPath = 'http://'+app.config['API_IP']+':5000/model/predict'

    with open(img_file_path,'rb') as img:
        img_data = img.read()
        payload = {'image': (img_file_path, img_data, 'image/png')}
    #response = requests.post(modelPath, headers=headers, files=files)
    response = requests.post(modelPath, files=payload)
    print(response.content)
    # Display image in Flask application web page
    return render_template('show_image.html', user_image = img_file_path, prediction = response.content)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0")