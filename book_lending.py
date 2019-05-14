from datetime import datetime
import random

class Book:

    on_shelf = []
    on_loan = []
    overdue_books = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def borrow(self):
        if self.lent_out():
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def return_to_library(self):
        if self.lent_out():
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            due_date = None
            return True
        else: 
            return False

    def lent_out(self):
        for book in Book.on_loan:
            if book == self:
                return True
        return False

    @classmethod
    def create(cls, title, author, ispn):
        book = Book(title, author, ispn)
        cls.on_shelf.append(book)
        return book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds 
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue(cls):
        for book in overdue_books:
            if Book.current_due_date() < datetime.now():
                Book.overdue_books.append(book)
            else:
                return False
        return False

    @classmethod
    def browse(cls):
        temp = random.choice(cls.on_shelf)
        return temp


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")

print(Book.browse().title)
print(Book.browse().title)

print(len(Book.on_shelf)) 
print(len(Book.on_loan)) 

print(sister_outsider.lent_out())

print(sister_outsider.borrow())

print(sister_outsider.lent_out())

print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1

print(sister_outsider.lent_out()) # True

print(sister_outsider.borrow()) # False

print(sister_outsider.current_due_date()) # 2017-02-25 20:52:20 -0500 (this value will be different for you)

print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False

print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0