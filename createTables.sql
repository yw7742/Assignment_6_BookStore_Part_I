PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS category;

CREATE TABLE category (
    categoryId INTEGER PRIMARY KEY,
    categoryName TEXT NOT NULL UNIQUE CHECK(length(trim(categoryName)) > 0),
    categoryImage TEXT NOT NULL CHECK(length(trim(categoryImage)) > 0)
);

CREATE TABLE book (
    bookId INTEGER PRIMARY KEY,
    categoryId INTEGER NOT NULL,
    title TEXT NOT NULL CHECK(length(trim(title)) > 0),
    author TEXT NOT NULL CHECK(length(trim(author)) > 0),
    isbn TEXT NOT NULL UNIQUE CHECK(length(trim(isbn)) > 0),
    price REAL NOT NULL CHECK(price >= 0),
    image TEXT NOT NULL CHECK(length(trim(image)) > 0),
    readNow INTEGER NOT NULL DEFAULT 0 CHECK(readNow IN (0, 1)),
    FOREIGN KEY (categoryId) REFERENCES category(categoryId)
);
COMMIT;
