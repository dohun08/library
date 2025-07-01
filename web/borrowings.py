from fastapi import Path
from fastapi import APIRouter, Body
from service import borrowings as service

router = APIRouter(prefix="/borrows")
@router.post("")
def borrow_book(req : dict = Body(...)) :
    return service.borrow_book(req)

@router.get("/month/{borrow_month}")
def get_borrows_books(borrow_month : int = Path(...)) :
    return service.get_borrows(borrow_month)

@router.get("/{borrower}/books")
def get_books(borrower : str) :
    return service.get_my_borrow_books(borrower)