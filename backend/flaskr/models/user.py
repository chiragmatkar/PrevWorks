from application.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(1000))
    sname = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    def __init__(self, email, fname, sname,password):
        self.email = email
        self.fname = fname
        self.sname = sname
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
