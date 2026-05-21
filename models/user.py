from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    email = db.Column(db.String(200), nullable = False, unique = True)
    password = db.Column(db.String(200), nullable = False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    date = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(10), nullable = False)
    
    __table_args__ = ( 
                        db.UniqueConstraint("user_id" , "date"),
                        )