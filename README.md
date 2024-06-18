# Library Management System

This is a simple Library Management System written in Python. It allows you to manage books and borrowers, and perform various operations such as adding, removing, borrowing, and returning books.

## Classes and Methods

### Book
Represents a book in the library.

#### Attributes:
- `title`: The title of the book.
- `author`: The author of the book.
- `isbn`: The ISBN of the book.
- `genre`: The genre of the book.
- `quantity`: The number of copies available.

#### Methods:
- `update_info(title=None, author=None, isbn=None, genre=None, quantity=None)`: Updates the book's information.
- `__str__()`: Returns a string representation of the book.

### Borrower
Represents a borrower in the library.

#### Attributes:
- `name`: The name of the borrower.
- `contact_details`: The contact details of the borrower.
- `membership_id`: The membership ID of the borrower.

#### Methods:
- `update_info(name=None, contact_details=None)`: Updates the borrower's information.
- `__str__()`: Returns a string representation of the borrower.

### Library
Represents the library itself.

#### Attributes:
- `books`: A dictionary of books in the library, keyed by ISBN.
- `borrowers`: A dictionary of borrowers in the library, keyed by membership ID.
- `borrowed_books`: A dictionary of borrowed books, keyed by a tuple of (ISBN, membership ID).

#### Methods:
- `add_book(book)`: Adds a book to the library.
- `remove_book(isbn)`: Removes a book from the library by ISBN.
- `add_borrower(borrower)`: Adds a borrower to the library.
- `remove_borrower(membership_id)`: Removes a borrower from the library by membership ID.
- `borrow_book(isbn, membership_id, due_date)`: Borrows a book for a borrower.
- `return_book(isbn, membership_id)`: Returns a borrowed book.
- `search_books(title=None, author=None, genre=None)`: Searches for books by title, author, or genre.
- `show_availability(isbn)`: Shows the availability of a book by ISBN.

## Example Usage

```python
# Create a library instance
library = Library()

# Create a book instance
book1 = Book('1984', 'George Orwell', '123456789', 'Dystopian', 5)

# Add the book to the library
library.add_book(book1)

# Create a borrower instance
borrower1 = Borrower('John Doe', '123 Main St', 'ID001')

# Add the borrower to the library
library.add_borrower(borrower1)

# Borrow the book
library.borrow_book('123456789', 'ID001', '2024-07-01')

# Show the availability of the book
library.show_availability('123456789')

# Return the book
library.return_book('123456789', 'ID001')

# Search for a book
library.search_books(title='1984')
