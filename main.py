class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability_status = True

    def update_status(self, status):
        self.availability_status = status

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available: {self.availability_status}")

class Member:
    def __init__(self, name, id, borrowed_books = []):
        self.name = name
        self.id = id
        self.books = borrowed_books

    def borrow_book(self, book):
        if book.availability_status:
            book.update_status(False)
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.update_status(True)
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

class LibraryStaff:
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Book '{book.title}' added by {self.name}")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"Book '{book.title}' removed by {self.name}")
        else:
            print(f"Book '{book.title}' not found in the library")

    def update_book_info(self, book, title=None, author=None):
        if title:
            book.title = title
        if author:
            book.author = author
        
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def search_book(self, title=None, author=None, isbn=None):
        results = []
        for book in self.books:
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
            elif isbn and isbn == book.isbn:
                results.append(book)
        return [book.display_info() for book in results]

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered with ID {member.member_id}")      
