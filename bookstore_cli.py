# Yi Wang
# Bookstore Part I

import math
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().with_name("bookstore.db")


def show_rows(cursor):
    rows = cursor.fetchall()
    if not rows:
        print("No results found.")
        return
    columns = []
    for column in cursor.description:
        columns.append(column[0])
    print(" | ".join(columns))
    print("-" * 80)
    for row in rows:
        values = []
        for value in row:
            values.append(str(value))
        print(" | ".join(values))
    print(f"{len(rows)} result(s).")


def read_text(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("Text fields cannot be empty.")
    return value


def read_id(prompt):
    value = int(input(prompt).strip())
    if value <= 0:
        raise ValueError("IDs must be positive integers.")
    return value


def read_price(prompt):
    value = float(input(prompt).strip())
    if not math.isfinite(value) or value < 0:
        raise ValueError("Price must be a finite, nonnegative number.")
    return round(value, 2)


def view_categories(connection):
    cursor = connection.execute(
        "SELECT categoryId, categoryName, categoryImage FROM category ORDER BY categoryId"
    )
    show_rows(cursor)


def view_books(connection):
    cursor = connection.execute("""
        SELECT bookId, categoryId, title, author, isbn, price, image, readNow
        FROM book ORDER BY title
    """)
    show_rows(cursor)


def view_books_in_category(connection):
    category_id = read_id("Enter category id: ")
    cursor = connection.execute("""
        SELECT book.bookId, book.title, book.author, book.price, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ? ORDER BY book.title
    """, (category_id,))
    show_rows(cursor)


def search_by_title(connection):
    keyword = read_text("Enter a title keyword: ")
    cursor = connection.execute("""
        SELECT bookId, title, author, price FROM book
        WHERE title LIKE ? ORDER BY title
    """, ("%" + keyword + "%",))
    show_rows(cursor)


def search_by_author(connection):
    # Extra feature: search for books by author.
    keyword = read_text("Enter an author keyword: ")
    cursor = connection.execute("""
        SELECT bookId, title, author, price FROM book
        WHERE author LIKE ? ORDER BY author, title
    """, ("%" + keyword + "%",))
    show_rows(cursor)


def add_book(connection):
    category_id = read_id("Enter category id: ")
    title = read_text("Enter title: ")
    author = read_text("Enter author: ")
    isbn = read_text("Enter ISBN: ")
    price = read_price("Enter price: ")
    image = read_text("Enter image filename: ")
    read_now = int(input("Enter readNow (0 or 1): ").strip())
    if read_now not in (0, 1):
        raise ValueError("readNow must be 0 or 1.")
    # Each write commits on success and rolls back if a database error occurs.
    with connection:
        cursor = connection.execute("""
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (category_id, title, author, isbn, price, image, read_now))
    print(f"Book added. ID: {cursor.lastrowid}")


def update_price(connection):
    book_id = read_id("Enter book id: ")
    price = read_price("Enter new price: ")
    with connection:
        cursor = connection.execute(
            "UPDATE book SET price = ? WHERE bookId = ?", (price, book_id)
        )
    if cursor.rowcount == 0:
        print("No book found.")
    else:
        print("Price updated.")


def delete_book(connection):
    book_id = read_id("Enter book id to delete: ")
    with connection:
        cursor = connection.execute("DELETE FROM book WHERE bookId = ?", (book_id,))
    if cursor.rowcount == 0:
        print("No book found.")
    else:
        print("Book deleted.")


def print_menu():
    print("\nBookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Quit")
    print("9. Search books by author")


def main():
    if not DB_PATH.is_file():
        print("Database missing. Follow README.md to create bookstore.db first.")
        return
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        print("Welcome to the Bookstore")
        while True:
            print_menu()
            choice = input("Choose an option: ").strip()
            try:
                if choice == "1":
                    view_categories(connection)
                elif choice == "2":
                    view_books(connection)
                elif choice == "3":
                    view_books_in_category(connection)
                elif choice == "4":
                    search_by_title(connection)
                elif choice == "5":
                    add_book(connection)
                elif choice == "6":
                    update_price(connection)
                elif choice == "7":
                    delete_book(connection)
                elif choice == "8":
                    print("Goodbye!")
                    break
                elif choice == "9":
                    search_by_author(connection)
                else:
                    print("Invalid option. Choose a number from 1 to 9.")
            except ValueError as error:
                print(f"Invalid input: {error}")
            except sqlite3.IntegrityError as error:
                print(f"Database constraint error: {error}")
            except sqlite3.Error as error:
                print(f"Database error: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
