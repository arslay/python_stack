from flask import Flask, render_template, redirect, request, session
import random
app=Flask(__name__)
app.secret_key='superSneaky'

@app.route('/')
def index():
    if 'correct' not in session:
        session['correct']=random.randint(0,100)
    if 'result' not in session:
        result='no guess yet' 
    else:
        result=session['result']
    return render_template('greatNumberGame.html', result=result)

@app.route('/guessnumber', methods=['POST'])
def guessnumber():
    if request.form['guess']=='':
        session['result']='TOO LOW'
    elif int(request.form['guess'])>session['correct']:
        session['result']='TOO HIGH'
    elif int(request.form['guess'])<session['correct']:
        session['result']='TOO LOW'
    else:
        session['result']='CORRECT'
    return redirect('/')

@app.route('/reset')
def reset():
    session['correct']=random.randint(0,100)
    result='no guess yet'
    return render_template('greatNumberGame.html', result=result)

app.run(debug=True)
