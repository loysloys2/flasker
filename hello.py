from flask import Flask, render_template


#Create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#	return "<h1>Hello World!</h1>"


def index():
	first_name = "John"
	stuff = "This is bold Text"

	favorite_pizza = ["Pepperoni", "Cheese", 41]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		favorite_pizza=favorite_pizza)

@app.route('/user/<name>')	

def user(name):
	return render_template("user.html", user_name=name)


#create custom error pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal Server Error thing
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
