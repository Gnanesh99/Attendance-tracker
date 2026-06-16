#IMPORTS
from flask import Flask
from dotenv import load_dotenv
from extensions import db,bcrypt
import os

#DOT ENV FILE 
load_dotenv()

#APP DECLARATION AND CONFIGURATION OF SECRET KEY AND DATABASE TO FLASK
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

#INITIALIZING DB AND BCRYPT
db.init_app(app)
bcrypt.init_app(app)

#CREATING DB TABLES WITH RESPECT TO THE CONTEXT OF THE SPECIFIC APP
from models.user import User,Attendance
with app.app_context():
    db.create_all()
    
#ROUTES IMPORT
from routes.attendance import attendance
from routes.auth import auth

#BLUEPRINTS
app.register_blueprint(attendance)
app.register_blueprint(auth)

#RUN THE APP
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)