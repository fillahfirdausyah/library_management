from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from ninja import Router, Body, Path

from api.v1.books.services.books_service import BooksService

from api.v1.books.schemas.books_schema import (
    BooksBodySchema,
    BooksGetByIdPathSchema
)

books_router = Router()
books_router.tags = ["Books"]

service = BooksService()

@books_router.get("")
def get_books(request: WSGIRequest):

    result = service.get_books()

    return JsonResponse(data={
        "message": "Books retrieved successfully",
        "payload": result
    })


@books_router.get("/{id}")
def get_book_by_id(request: WSGIRequest, path: BooksGetByIdPathSchema = Path(...)):

    result = service.get_book_by_id(id=path.id)

    return JsonResponse(data={
        "message": "Book retrieved successfully",
        "payload": result
    })


@books_router.post("")
def create_book(request: WSGIRequest, body: BooksBodySchema = Body(...)):

    result = service.create_book(
        author_id=body.author, 
        title=body.title, 
        description=body.description, 
        publish_date=body.publish_date)

    return JsonResponse(data={
        "message": "Book created successfully",
        "payload": result
    })


@books_router.put("/{id}")
def update_book_by_id(
    request: WSGIRequest, 
    path: BooksGetByIdPathSchema = Path(...),
    body: BooksBodySchema = Body(...)):

    result = service.update_book_by_id(
        id=path.id,
        author_id=body.author, 
        title=body.title, 
        description=body.description, 
        publish_date=body.publish_date)
    
    return JsonResponse(data={
        "message": "Book updated successfully",
        "payload": result
    })


@books_router.delete("/{id}")
def delete_book_by_id(request: WSGIRequest, path: BooksGetByIdPathSchema = Path(...)):

    result = service.delete_book_by_id(id=path.id)

    return JsonResponse(data={
        "message": "Book deleted successfully",
    })