from datetime import datetime, timedelta

class LibraryManager:
    def __init__(self):
        self.books_dict = []
        self.borrowers_list = []
        self.borrowed_books = {}

    def add_book(self, book):
        for each_book in self.books_dict:
            if book['isbn'] == each_book['isbn']:
                each_book['quantity'] += book['quantity']
                print(f"Quantity of '{book['title']}' updated in library.")
                return
        self.books_dict.append(book)
        print(f"Book '{book['title']}' added to library.")

    def remove_book(self, isbn):
        for book in self.books_dict:
            if isbn == book['isbn']:
                self.books_dict.remove(book)
                print(f"Book with ISBN {isbn} removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def search_book(self, title):
        found = False
        for book in self.books_dict:
            if title.lower() == book['title'].lower():
                print(f"Book '{book['title']}' found.")
                found = True
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        for book in self.books_dict:
            if isbn == book['isbn']:
                if title:
                    book['title'] = title
                if author:
                    book['author'] = author
                if genre:
                    book['genre'] = genre
                if quantity is not None:
                    book['quantity'] = quantity
                print(f"Book with ISBN {isbn} has been updated.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def add_borrower(self, borrower):
        self.borrowers_list.append(borrower)
        print(f'Borrower "{borrower["name"]}" added to the system.')

    def remove_borrower(self, membership_id):
        for borrower in self.borrowers_list:
            if membership_id == borrower['membership_id']:
                self.borrowers_list.remove(borrower)
                print(f'Borrower with membership ID {membership_id} removed from the system.')
                return
        print(f'Borrower with membership ID {membership_id} not found.')

    def search_borrower(self, name):
        found = False
        for borrower in self.borrowers_list:
            if name.lower() == borrower['name'].lower():
                print(f'Borrower "{borrower["name"]}" found.')
                found = True
        if not found:
            print(f'Borrower "{name}" not found in the system.')

    def update_borrower(self, membership_id, name=None, contact_details=None):
        for borrower in self.borrowers_list:
            if membership_id == borrower['membership_id']:
                if name:
                    borrower['name'] = name
                if contact_details:
                    borrower['contact_details'] = contact_details
                print(f'Borrower with membership ID {membership_id} has been updated.')
                return
        print(f'Borrower with membership ID {membership_id} not found.')

    def borrow_book(self, isbn, membership_id, due_date):
        for book in self.books_dict:
            if isbn == book['isbn']:
                if book['quantity'] > 0:
                    self.books_dict[self.books_dict.index(book)]['quantity'] -= 1
                    self.borrowed_books[(isbn, membership_id)] = due_date
                    print(f'Book with ISBN {isbn} borrowed by {membership_id}.')
                    return
                else:
                    print(f'All copies of Book with ISBN {isbn} are currently borrowed.')
                    return
        print(f'Book with ISBN {isbn} not found.')

    def return_book(self, isbn, membership_id):
        if (isbn, membership_id) in self.borrowed_books:
            del self.borrowed_books[(isbn, membership_id)]
            for book in self.books_dict:
                if isbn == book['isbn']:
                    self.books_dict[self.books_dict.index(book)]['quantity'] += 1
                    print(f'Book with ISBN {isbn} returned by {membership_id}.')
                    return
        print(f'Book with ISBN {isbn} not borrowed by {membership_id}.')

    def check_overdue_books(self, current_date=None):
        if not current_date:
            current_date = datetime.now().date()
        
        overdue_books = []
        for (isbn, membership_id), due_date in self.borrowed_books.items():
            if current_date > due_date:
                overdue_books.append((isbn, membership_id))
        
        if overdue_books:
            print("Overdue Books:")
            for isbn, membership_id in overdue_books:
                print(f"Book with ISBN {isbn} borrowed by {membership_id} is overdue.")
        else:
            print("No overdue books.")

    def show_all_books(self):
        if self.books_dict:
            print("Books in Library:")
            for book in self.books_dict:
                print(f"{book['title']} by {book['author']} | ISBN: {book['isbn']} | Genre: {book['genre']} | Quantity: {book['quantity']}")
        else:
            print("No books in Library.")

    def show_all_borrowers(self):
        if self.borrowers_list:
            print("Borrowers in System:")
            for borrower in self.borrowers_list:
                print(f"{borrower['name']} | Membership ID: {borrower['membership_id']} | Contact Details: {borrower['contact_details']}")
        else:
            print("No borrowers in System.")

