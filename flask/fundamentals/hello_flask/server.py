from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', phrase="hello", times=5)

@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
