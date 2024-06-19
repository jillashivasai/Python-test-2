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
- `books_dict`: A list of books in the library.
- `borrowers_list`: A list of borrowers in the library.
- `borrowed_books`: A dictionary of borrowed books, keyed by a tuple of (ISBN, membership ID).

#### Methods:
- `add_book(book)`: Adds a book to the library.
- `remove_book(isbn)`: Removes a book from the library by ISBN.
- `add_borrower(borrower)`: Adds a borrower to the library.
- `remove_borrower(membership_id)`: Removes a borrower from the library by membership ID.
- `borrow_book(isbn, membership_id, due_date)`: Borrows a book for a borrower.
- `return_book(isbn, membership_id)`: Returns a borrowed book.
- `search_book(title)`: Searches for a book by title.
- `search_borrower(name)`: Searches for a borrower by name.
- `update_book(isbn, title=None, author=None, genre=None, quantity=None)`: Updates book information.
- `update_borrower(membership_id, name=None, contact_details=None)`: Updates borrower information.
- `show_all_books()`: Displays all books in the library.
- `show_all_borrowers()`: Displays all borrowers in the library.
- `check_overdue_books(current_date=None)`: Checks for overdue books.

## Example Usage

```python
# Example usage code can go here...
