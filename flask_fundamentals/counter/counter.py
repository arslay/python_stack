
from flask import Flask, render_template,request,redirect,session,app  # Import Flask to allow us to create our app, and import


app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
app.secret_key = "lars"
@app.route('/')                          
def displayForm():
  session['counter']+=1
  return render_template('index.html',counter=session['counter'])    # Render the template and return it!

@app.route('/addTwoButton')
def addTwo():
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def refresh():
  session['counter']=0
  return redirect('/')

#@app.route('/users/<username>/<id>')
#def show_user_profile(username, id):
#  print(username)
#  print(username)
#  return render_template("user.html")

app.run(debug=True)                       # Run the app in debug mode.
