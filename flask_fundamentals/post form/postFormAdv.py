from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>')


#Build a flask application that accepts a form submission, 
#redirects, and presents the submitted data on a results page.
#Hint: Although we've told you never to render from a post route, 
# you'll need to do so for this assignment
# We'll show you tools to avoid doing so soon.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.
@app.route('/users/<username>/<id>))
def show_user_profile(username, id):
	print username
	print id
    return render_template("user.html")