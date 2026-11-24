# Bookstore Part I

Name: Yi Wang

This bookstore has four categories: Classic Fiction, Fantasy, Science Fiction,
and Nonfiction. Each category starts with three books, for a total of twelve.
The books have real titles and authors. Prices are sample store prices.
Image filenames and readNow values are sample data; images are not displayed.

## Files

- `createTables.sql` creates the category and book tables.
- `insertRows.sql` adds the sample data.
- `bookstore.db` is the database, already populated with the sample data.
- `bookstore_cli.py` runs the menu.
- `README.md` contains the instructions.

## Create the database

Use Python 3. No extra Python packages are needed.
Open a terminal in the bookstore folder. If the SQLite shell is installed, run:

```bash
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql
```

These commands reset the database and remove previous changes. Run them in this
order, and only run the insert script once after creating the tables.

If the SQLite shell is not installed, start Python with `python3` and enter:

```python
import sqlite3

connection = sqlite3.connect("bookstore.db")
with open("createTables.sql", encoding="utf-8") as file:
    connection.executescript(file.read())

with open("insertRows.sql", encoding="utf-8") as file:
    connection.executescript(file.read())

connection.close()
exit()
```

## Run the program

```bash
python3 bookstore_cli.py
```

On Windows, use `python` instead of `python3` if needed.
The program opens the database next to the Python file.

## Menu

1. View all categories
2. View all books
3. View books in a category
4. Search books by title
5. Add a new book
6. Update a book price
7. Delete a book
8. Quit
9. Search books by author (additional feature)

For example, category ID `2` shows the fantasy books. Searching for the title
`Hobbit` gives one book. Searching for the author `Tolkien` gives two books.
Search uses SQL LIKE with a keyword surrounded by `%`. SQL wildcards `%` and `_`
also work in the search input.

## Notes

The book table links to the category table using categoryId. The program enables
foreign keys and uses `?` placeholders for user input. Each successful change is
saved immediately. An ISBN cannot be repeated, prices cannot be negative, and
readNow must be 0 or 1. Invalid inputs show an error message and return to the menu.

Based on the course example:
https://github.com/markr-nyu/Assignment_6_BookStore_Part_I
