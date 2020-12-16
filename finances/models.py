from finances.ext.database import db


class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), nullable=False)
    month = db.Column(db.String(2), nullable=False) 
    date = db.Column(db.String(2), nullable=False)

    content = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, default=0)
    isFixed = db.Column(db.Boolean, default = False)

'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
'''