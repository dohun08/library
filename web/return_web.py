from fastapi import APIRouter, Body
from service import return_service as service

router = APIRouter(prefix="/return")

@router.post("")
def return_book(req : dict = Body(...)):
    return service.return_book(req)