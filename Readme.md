<h1>Library database</h1>

<h2>About the project</h2>
<hr>
<p>This Software has the objective of training the basics of database CRUD, utilizing Flask resources to structure the front and the back end, and the SLQAlchemy to deal with the database features</p>

<p>There are three classes distributed in 2 files: <br>
<ul><li>book.py: This file contains the class <b>Book</b>, which is assigned to structure the columns of the <b>Book</b> table and organize the received data to insert into its respective table.</li></ul>
<ul><li>forms.py: This file contains 2 Classes, the <b>AddForm</b> and <b>EditForm</b>. They're using the <b>FlaskForm</b> features to create and manipulate forms of this software, instead of the form resources from HTML. </li></ul>
<h2>How it works</h2>
<hr>
At the home page <b>(index.html)</b>, there is a button to add one book to the database, and on the following page <b>(add.html)</b> a form will be displayed to fill with the data of the book that will be inserted on the database. After submiting the form successfully, the user will be redirected to the home page, and will be seeing the data displayed on this page. There's available one botton on either side of each row on the list of books, the <b>Edit rating</b> and <b>Delete entry</b>

</p>
