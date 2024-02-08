from app import db




# create /set table columns
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(80),unique=False,nullable=True)
    password = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    mobile =db.Column(db.String(15),nullable=False)
    city =db.Column(db.Text(50),nullable=False)
    designation =db.Column(db.String(50),nullable=False)