from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>') # for a route '/say/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    if name.isalpha():
        return f"Hi {name}!"
    return "Invalid input"

@app.route('/repeat/<count>/<input>') # for a route '/repeat/____/____', two parameters in the url get passed as count and input
def repeat(count, input):
    if not (count.isdecimal() and input.isalpha()):
        return "Invalid input"
    icount = int(count)
    output = ''
    for x in range(icount):
        output += input + "<br>"
    return output

@app.errorhandler(404) # for a route not found
def not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
