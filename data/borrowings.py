from . import con, cur
def test():
    return "sqlite connect ok"

def set_available_book(book_id):
    sql = "UPDATE books SET available = 0 WHERE book_id = ?"
    try :
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

def borrow_create_book(book_id, author):
    sql = "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)"
    cur.execute(sql, (book_id, author))
    con.commit()
def get_borrows(month: int):
    # 2025년 + 2자리 월 문자열 만들기
    borrow_month = f"2025-{month:02d}"   # 예: 3 -> '2025-03'

    sql = """
    SELECT
        b.borrower,
        bk.title,
        bk.author
    FROM
        borrowings b
    JOIN
        books bk ON b.book_id = bk.book_id
    WHERE
        b.returned_at IS NULL
        AND strftime('%Y-%m', b.borrowed_at) = ?
    """
    cur.execute(sql, (borrow_month,))
    rows = cur.fetchall()
    return [
        {"borrower": row[0], "title": row[1], "author": row[2]}
        for row in rows
    ]

def delete_record(book_id, borrower):
    sql = "DELETE FROM borrowings WHERE book_id = ? AND borrower = ?"
    cur.execute(sql, (book_id, borrower))
    con.commit()