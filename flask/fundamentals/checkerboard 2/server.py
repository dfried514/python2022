from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def standard():
    return render_template("index.html", x=8, y=8,
        color1="black", color2="#E93F22")

@app.route('/<int:y>')
def withColumns(y):
    return render_template("index.html", x=8, y=y,
        color1="black", color2="#E93F22")

@app.route('/<int:x>/<int:y>')
def withColumnsAndRows(x, y):
    return render_template("index.html", x=x, y=y,
        color1="black", color2="#E93F22")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def withColumnsAndRowsAndColors(x, y, color1, color2):
    return render_template("index.html", x=x, y=y,
        color1=color1, color2=color2)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)
