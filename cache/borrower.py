from . import redis_client

def test():
    return "redis connect ok"

def create_borrow_cache(borrower, title):
    key = f"borrower:{borrower}:books"
    redis_client.sadd(key, title)
    print(f"{borrower}님이 '{title}' 대출 목록에 추가되었습니다.")

def delete_book(title, borrower):
    key = f"borrower:{borrower}:books"
    removed = redis_client.srem(key, title)
    if removed:
        print(f"{borrower}님 대출 목록에서 '{title}'이 제거되었습니다.")
    else:
        print(f"{borrower}님 대출 목록에 '{title}'이 없습니다.")

def get_borrows(borrower):
    key = f"borrower:{borrower}:books"
    books = redis_client.smembers(key)
    books_list = [b.decode() for b in books]
    return {
        "borrower": borrower,
        "books": books_list
    }