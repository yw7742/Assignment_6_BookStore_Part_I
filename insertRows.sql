PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Classic Fiction', 'classic-fiction.jpg'),
(2, 'Fantasy', 'fantasy.jpg'),
(3, 'Science Fiction', 'science-fiction.jpg'),
(4, 'Nonfiction', 'nonfiction.jpg');

-- Prices are illustrative store prices, not live retail quotations.
-- Image names and readNow flags are sample metadata for this assignment.
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Pride and Prejudice', 'Jane Austen', '9780141439518', 12.00, 'pride-and-prejudice.jpg', 1),
(2, 1, 'The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 16.00, 'the-great-gatsby.jpg', 1),
(3, 1, 'To Kill a Mockingbird', 'Harper Lee', '9780061120084', 18.99, 'to-kill-a-mockingbird.jpg', 0),
(4, 2, 'The Hobbit', 'J. R. R. Tolkien', '9780547928227', 15.99, 'the-hobbit.jpg', 0),
(5, 2, 'The Fellowship of the Ring', 'J. R. R. Tolkien', '9780547928210', 18.99, 'the-fellowship-of-the-ring.jpg', 0),
(6, 2, 'A Game of Thrones', 'George R. R. Martin', '9780553593716', 10.99, 'a-game-of-thrones.jpg', 0),
(7, 3, 'Dune', 'Frank Herbert', '9780441172719', 10.99, 'dune.jpg', 0),
(8, 3, 'The Left Hand of Darkness', 'Ursula K. Le Guin', '9780441478125', 10.99, 'the-left-hand-of-darkness.jpg', 1),
(9, 3, 'The Martian', 'Andy Weir', '9780553418026', 17.00, 'the-martian.jpg', 0),
(10, 4, 'A Brief History of Time', 'Stephen Hawking', '9780553380163', 18.00, 'a-brief-history-of-time.jpg', 1),
(11, 4, 'The Immortal Life of Henrietta Lacks', 'Rebecca Skloot', '9781400052189', 18.00, 'henrietta-lacks.jpg', 0),
(12, 4, 'Educated', 'Tara Westover', '9780399590504', 28.00, 'educated.jpg', 0);
COMMIT;
