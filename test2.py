class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_info(self, title=None, author=None, isbn=None, genre=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        if genre:
            self.genre = genre
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Genre: {self.genre} | Quantity: {self.quantity}"


class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id

    def update_info(self, name=None, contact_details=None):
        if name:
            self.name = name
        if contact_details:
            self.contact_details = contact_details

    def __str__(self):
        return f"{self.name} | Contact: {self.contact_details} | Membership ID: {self.membership_id}"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].quantity += book.quantity
        else:
            self.books[book.isbn] = book
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f'Book with ISBN {isbn} removed from the library.')
        else:
            print(f'Book with ISBN {isbn} not found.')

    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower
        print(f'Borrower "{borrower.name}" added to the system.')

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(f'Borrower with membership ID {membership_id} removed from the system.')
        else:
            print(f'Borrower with membership ID {membership_id} not found.')

    def borrow_book(self, isbn, membership_id, due_date):
        if isbn in self.books and membership_id in self.borrowers and self.books[isbn].quantity > 0:
            self.books[isbn].quantity -= 1
            self.borrowed_books[(isbn, membership_id)] = due_date
            print(f'Book with ISBN {isbn} borrowed by {membership_id}.')
        else:
            print(f'Failed to borrow book with ISBN {isbn} for membership ID {membership_id}.')

    def return_book(self, isbn, membership_id):
        if (isbn, membership_id) in self.borrowed_books:
            del self.borrowed_books[(isbn, membership_id)]
            if isbn in self.books:
                self.books[isbn].quantity += 1
            print(f'Book with ISBN {isbn} returned by {membership_id}.')
        else:
            print(f'Failed to return book with ISBN {isbn} for membership ID {membership_id}.')

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
                print(book)
                print(f"Available copies: {book.quantity}")
        return results
    
    def show_availability(self,isbn):
        if isbn in self.books:
            book=self.books[isbn]
            print(f'Book "{book.title}" availability: {book.quantity} copies.')
        else:
            print(f'Book with ISBN {isbn} not found.')


library = Library()
book1 = Book('1984', 'George Orwell', '123456789', 'Dystopian', 5)
library.add_book(book1)
borrower1 = Borrower('John Doe', '123 Main St', 'ID001')
library.add_borrower(borrower1)
library.borrow_book('123456789', 'ID001', '2024-07-01')
library.show_availability('123456789')
library.return_book('123456789', 'ID001')
library.search_books(title='1984')
