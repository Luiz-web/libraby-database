from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField

class AddForm(FlaskForm):
    book_name = StringField('Book Name')
    book_author = StringField('Book Author')
    rating = FloatField('Rating')
    submit = SubmitField("Add Book")


class EditForm(FlaskForm):
    new_rating = FloatField('New Rating')
    submit = SubmitField("Update data")