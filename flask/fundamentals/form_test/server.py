from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

from flask import Flask, render_template, request, redirect # added request

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print("form name: ", request.form['name'])
    print("form email: ", request.form['email'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index router
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
