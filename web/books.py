from fastapi import APIRouter, Body
from service import books as service

router = APIRouter(prefix="/books")

@router.post("")
def test(data : dict = Body(...)):
    return service.create_book(data)

@router.get("")
def get_available() :
    return service.get_available()

@router.delete("/{book_id}")
def delete_book(book_id : int) :
    return service.delete_book(book_id)
