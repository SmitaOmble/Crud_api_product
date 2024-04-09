from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)