from fastapi import HTTPException, status
from data import borrowings as borrowings_data
from data import books as books_data
from cache import borrower as cache

def test():
    db_test = borrowings_data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}

def borrow_book(req) :
    try :
        book_id = books_data.get_book_id(req['title'])
        borrowings_data.set_available_book(book_id)
        cache.create_borrow_cache(req['borrower'], req['title'])
        borrowings_data.borrow_create_book(book_id, req['borrower'])
        return True
    except Exception as e:
        print("DB Error:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

def get_borrows(borrow_month) :
    return borrowings_data.get_borrows(borrow_month)

def get_my_borrow_books(borrower) :
    return cache.get_borrows(borrower)