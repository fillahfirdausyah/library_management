from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from ninja import Query, Router

from api.v1.authors.services.authors_service import AuthorsService

authors_router = Router()
authors_router.tags = ["Authors"]

service = AuthorsService()


@authors_router.get("")
def get_authors(request: WSGIRequest):

    result = service.get_authors()

    return JsonResponse(data={
        "message": "Authors retrieved successfully",
        "payload": result
    })