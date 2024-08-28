from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from ninja import Router, Body, Path

from api.v1.authors.services.authors_service import AuthorsService

from api.v1.authors.schemas.authors_schemas import (
    AuthorsBodySchema,
    AuthorsGetByIdPathSchema
)

authors_router = Router()
authors_router.tags = ["Authors"]

service = AuthorsService()


@authors_router.post("")
def create_author(request: WSGIRequest, body: AuthorsBodySchema = Body(...)):

    result = service.create_author(name=body.name, bio=body.bio, birth_date=body.birth_date)

    return JsonResponse(data={
        "message": "Author created successfully",
        "payload": result
    }, status=201)

@authors_router.get("")
def get_authors(request: WSGIRequest):

    result = service.get_authors()

    return JsonResponse(data={
        "message": "Authors retrieved successfully",
        "payload": result
    })

@authors_router.get("/{id}")
def get_author_by_id(request: WSGIRequest, path: AuthorsGetByIdPathSchema = Path(...)):

    result = service.get_author_by_id(id=path.id)

    return JsonResponse(data={
        "message": "Author retrieved successfully",
        "payload": result
    })

@authors_router.put("/{id}")
def update_author_by_id(
    request: WSGIRequest, 
    path: AuthorsGetByIdPathSchema = Path(...), 
    body: AuthorsBodySchema = Body(...)):

    result = service.update_author_by_id(
        id=path.id, 
        name=body.name, 
        bio=body.bio, 
        birth_date=body.birth_date)

    return JsonResponse(data={
        "message": "Author updated successfully",
        "payload": result
    })

@authors_router.delete("/{id}")
def delete_author_by_id(request: WSGIRequest, path: AuthorsGetByIdPathSchema = Path(...)):

    result = service.delete_author_by_id(id=path.id)

    return JsonResponse(data={
        "message": "Author deleted successfully",
    })

@authors_router.get("/{id}/books")
def get_books_by_author_id(request: WSGIRequest, path: AuthorsGetByIdPathSchema = Path(...)):

    result = service.get_books_by_author_id(id=path.id)

    return JsonResponse(data={
        "message": "Books retrieved successfully",
        "payload": result
    })