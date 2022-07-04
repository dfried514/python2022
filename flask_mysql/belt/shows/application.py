from flask_app import application
from flask_app.controllers import users, shows, likes
 
if __name__ == "__main__":
    application.run(debug=True)