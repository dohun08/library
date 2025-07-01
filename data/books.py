from pydantic.v1 import BaseModel

from data import cur, con

class Available(BaseModel) :
    title : str
    author : str

def create_book(data):
    sql = "INSERT INTO books (title, author) VALUES (?, ?)"
    try:
        cur.execute(sql, (
            data["title"],
            data["author"],
        ))
        con.commit()
        return True
    except Exception as e:
        print("DB Error:", e)
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )


def get_available():
    sql = "SELECT title, author FROM books WHERE available = 1"
    cur.execute(sql)
    rows = cur.fetchall()
    # Available 객체로 변환
    books = [Available(title=row[0], author=row[1]) for row in rows]
    return books


def delete_book(book_id) :
    sql = "DELETE FROM books WHERE available = 1 and book_id = ?"
    try:
        cur.execute(sql, (book_id,))
        con.commit()
        return True
    except Exception as e:
        print("DB Error:", e)
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

def get_book_id(title: str):
    sql = "SELECT book_id FROM books WHERE title = ?"
    cur.execute(sql, (title,))
    rows = cur.fetchall()
    return rows[0][0]

def add_available(book_id):
    sql = "UPDATE books SET available = 1 WHERE book_id = ?"
    cur.execute(sql, (book_id,))
    con.commit()