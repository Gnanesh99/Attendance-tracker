from flask import Blueprint,render_template,session,request,redirect,url_for
from datetime import date
from extensions import db,bcrypt
from models.user import User,Attendance
attendance = Blueprint("attendance",__name__)

from utils import login_required

@attendance.route("/dashboard",methods=["GET"])
@login_required
def dashboard():
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    today = date.today()    
    existing = Attendance.query.filter_by(user_id=user_id, date=today).first()
    records = Attendance.query.filter_by(user_id=user_id).order_by(Attendance.date.desc()).all()
    total = len(records)
    present_count = len([r for r in records if r.status in ["present","late"]])
    percentage = round((present_count / total) * 100, 2) if total > 0 else 0
    return render_template("dashboard.html", user=user,today=today,existing=existing,records=records,percentage=percentage)
    
@attendance.route("/mark",methods=["POST"])
@login_required
def mark_attendance():
    user_id = session.get("user_id")
    today = date.today()
    existing = Attendance.query.filter_by(user_id=user_id, date=today).first()
    user = User.query.get(user_id)
    records = Attendance.query.filter_by(user_id=user_id).all()
    total = len(records)
    present_count = len([r for r in records if r.status in ["present","late"]])
    percentage = round((present_count / total) * 100, 2) if total > 0 else 0
    if existing:
        return render_template("dashboard.html", user=user,existing=existing,records=records,percentage=percentage,error="Already Marked!")
    status = request.form["status"]
    if status not in ["present","absent","late"]:
        return render_template("dashboard.html", user=user,existing=existing,records=records,percentage=percentage,error="Invalid Status!")
    new_attendance = Attendance(user_id=user_id,date=today,status=status)
    db.session.add(new_attendance)
    db.session.commit()
    return redirect(url_for("attendance.dashboard"))
    