
from flask import Flask, render_template,request,redirect,session  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def displayForm():
  return render_template('index.html')    # Render the template and return it!

@app.route('/ninja')
def newUser():
    print('got post info')
    return render_template('ninja.html')


@app.route('/ninja/<color>')
def newUserColor(color):
    if(color is 'blue' or 'orange' or 'red' or 'purple'):
      session['color']=color
    else:
      session['color']='null'
    print('got post info')
    return render_template('ninjaColor.html',color=color)
    #return redirect('/')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codizngdojo.com')

#@app.route('/users/<username>/<id>')
#def show_user_profile(username, id):
#  print(username)
#  print(username)
#  return render_template("user.html")

app.run(debug=True)                       # Run the app in debug mode.

