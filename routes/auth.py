from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db, bcrypt
from models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
    return redirect(url_for("auth.login"))    

@auth.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            return render_template("register.html", error="Email Already Exists!")
        hashed_pw=bcrypt.generate_password_hash(password).decode("utf-8")
        new_user=User(username=username,email=email,password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()       
        return redirect("/login")
    if request.method=="GET":
        return render_template("register.html")

@auth.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        user = User.query.filter_by(email=email).first()
        if not user:
            return render_template("login.html", error="Invalid Email or Password!")
        if bcrypt.check_password_hash(user.password,password):
            session["user_id"]=user.id
            return redirect(url_for("attendance.dashboard"))
        else:
            return render_template("login.html", error="Invalid Email or Password!")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
