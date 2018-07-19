from flask import Flask, render_template,request,redirect  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def displayForm():
  return render_template('index.html')    # Render the template and return it!

@app.route('/users',methods=['POST'])
def newUser():
    print('got post info')
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']
    return render_template('result.html',name=name,location=location,language=language,comment=comment)
    #return redirect('/')

#@app.route('/users/<username>/<id>')
#def show_user_profile(username, id):
#  print(username)
#  print(username)
#  return render_template("user.html")

app.run(debug=True)                       # Run the app in debug mode.