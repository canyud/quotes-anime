from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AnimeQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anime = db.Column(db.String(255), nullable=False)
    character = db.Column(db.String(255), nullable=False)
    quote = db.Column(db.Text, nullable=False)
