class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return (f"{self.title} is {status}")
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def __str__(self):
        books_list = ",".join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return (f"Member: {self.name} | Borrowed: {books_list}")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book Added: {book.title}")

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if book and book.is_available:
            Book.is_available = False
            member.borrowed_books.append(book_title)
            print(f"Success! {member_name} borrowed '{book_title}'.\n")
        else:
            print(f"Error. {book_title} is unavailable or doesn't exist.")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if member:
            for book in member.borrowed_books:
                if book_title == book_title:
                    Book.is_available = True
                    member.borrowed_books.remove(book_title)
                    print(f"Success! {member_name} returned {book_title}.")
    
    def display_books(self):
        for book in self.books:
            print(book)


manukau_library = Library()

alice = Member("Alice")
john = Member("John")
manukau_library.add_member(john)
manukau_library.add_member(alice)

manukau_library.add_book(Book("Introduction to IT", "Steve Jobs"))
manukau_library.add_book(Book("The Fall of the Ten Kingdoms", "Musashi"))
manukau_library.display_books()

manukau_library.borrow_book("Alice", "The Fall of the Ten Kingdoms")
manukau_library.borrow_book("John", "Introduction to IT")
manukau_library.display_books()


manukau_library.return_book("Alice", "The Fall of the Ten Kingdoms")
manukau_library.display_books()

    