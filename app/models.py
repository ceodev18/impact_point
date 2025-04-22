from . import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    base_experience = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    types = db.Column(db.String(100))
    stats = db.Column(db.String(500))  # JSON string
    abilities = db.Column(db.String(200))
    sprite_url = db.Column(db.String(255))
    cry_url = db.Column(db.String(255))
