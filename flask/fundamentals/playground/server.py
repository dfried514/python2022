from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", x=0)

@app.route('/play')
def play():
    return render_template("index.html", x=3, color="blue")

@app.route('/play/<int:x>')
def play_x_times(x):
    return render_template("index.html", x=x, color="blue")

@app.route('/play/<int:x>/<string:color>')
def play_x_times_color(x, color):
    return render_template("index.html", x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)
