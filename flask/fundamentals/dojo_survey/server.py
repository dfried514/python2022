from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'magic_key'

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print('request.form', request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['preferred_role'] = request.form['preferred_role']
    session['operating_system'] = request.form.getlist('operating_system')
    session['comments'] = request.form['comments']
    return redirect(url_for("result"))

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
