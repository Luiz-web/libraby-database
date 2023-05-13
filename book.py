from sqlalchemy import String, Float, Integer, Column
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating
    
    id = db.Column(Integer, primary_key=True, unique=True, nullable=False, )
    title = db.Column(String(80), primary_key=False, unique=True, nullable=False)
    author = db.Column(String(80), primary_key=False, unique=False, nullable=False)
    rating = db.Column(Float, primary_key=False, unique=True, nullable=False)

    
