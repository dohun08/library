from data import books as books_data
from data import borrowings as borrowings_data
from cache import borrower as cache

def return_book(req):
    try :
        book_id = books_data.get_book_id(req['title'])
        books_data.add_available(book_id)
        borrowings_data.delete_record(book_id, req['borrower'])
        cache.delete_book(req['title'], req['borrower'])
        return True
    except Exception as e:
        print("DB Error:", e)
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )