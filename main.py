from fastapi import FastAPI

from web import borrowings as borrow_web
from web import books as book_web
from web import return_web
app = FastAPI()
app.include_router(borrow_web.router)
app.include_router(book_web.router)
app.include_router(return_web.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)