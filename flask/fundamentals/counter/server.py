from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'magic_key'

@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 1
    else: 
        session['count'] += 1
    if not 'visits' in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def update_count():
    if 'plus2' in request.form:
        session['count'] += 1
    elif 'reset' in request.form:
        session['count'] = 0
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment_count():
    if 'incrementBy' in request.form and request.form['incrementBy'].isdecimal():
        inc = int(request.form['incrementBy'])
        session['count'] += inc - 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
