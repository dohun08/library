from data import books as db

def create_book(data) :
    return db.create_book(data)

def get_available() :
    return db.get_available()

def delete_book(book_id : int) :
    return db.delete_book(book_id)