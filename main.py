from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from book import Book
from forms import AddForm, EditForm

app = Flask(__name__)
app.secret_key = 'A secret XD'
Bootstrap(app)
app.config ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection3.db"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', all_books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        books_database = Book(title=add_form.book_name.data, author=add_form.book_author.data, rating=add_form.rating.data)
        db.session.add(books_database)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=add_form)

@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    edit_form = EditForm()
    update_entry = db.session.query(Book).get(book_id)
    if edit_form.validate_on_submit():
        update_entry.rating = edit_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))   
    return render_template('edit.html', form=edit_form, update_entry=update_entry)

@app.route("/delete/<book_id>")
def delete(book_id):
    delete_entry = db.session.query(Book).get(book_id)
    db.session.delete(delete_entry)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

