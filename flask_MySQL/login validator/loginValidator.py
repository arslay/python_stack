from flask import Flask, render_template, redirect, request, session, flash
import random
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FULLNAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template('login.html', email='email')
@app.route('/process', methods=['POST'])
def submit():
    lenemail=len(request.form['email'])
    lenfirstName=len(request.form['firstName'])
    lenlastName=len(request.form['lastName'])
    lenpassword=len(request.form['password'])
    lenconfirmPassword=len(request.form['confirmPassword'])
    # easier to use a for loop to rotate thru these... how? 
    if lenemail<1 and lenfirstName<1 and  lenlastName<1 and lenpassword<1 and lenconfirmPassword<1 :
        flash("Make sure to enter all fields!")
    elif lenemail>120 and lenfirstName>120 and lenlastName>120 and lenpassword>120 and lenconfirmPassword>120:
        flash('Email too long =( ')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif not FULLNAME_REGEX.match(request.form['firstName']) or not FULLNAME_REGEX.match(request.form['lastName']) :
        flash("Name must not have numbers, sorry robots =(")
    elif not request.form['password'] == request.form['confirmPassword']:
        flash("Passwords must match!")
    else:
        flash('Success! Your name is {}'.format(request.form['firstName']))
    return redirect('/')
app.run(debug=True)