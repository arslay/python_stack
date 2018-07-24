#when you visit, "localhost:5000/" you are seeing the page we described above (in other words, we don't want to have to go to "/gold/index" or other URL to see this app).
#the forms are sent to "/process_money" and not any other URL.
#the activities are stored in the session. No need to store anything in the database. 

from flask import Flask, render_template, redirect, request, session
import random
app=Flask(__name__)
app.secret_key='superSneaky'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    return render_template('ninjaGold.html')

@app.route('/processMoney', methods=['POST'])
def processMoney():
    if request.form['building']=='farm':
        session['gold']=session['gold']+10
    if request.form['building']=='cave':
        session['gold']=session['gold']+5 
    if request.form['building']=='house':
        session['gold']=session['gold']+3     
    if request.form['building']=='casino':
        session['gold']=session['gold'] + random.randint(-50,50)
    return redirect('/')

    
app.run(debug=True)                       # Run the app in debug mode.