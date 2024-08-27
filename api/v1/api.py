from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.errors import AuthenticationError, ValidationError

from api.v1.exception.bad_request_exception import BadRequestException
from api.v1.exception.forbidden_exception import ForbiddenException
from api.v1.exception.notfound_exception import NotFoundException
from api.v1.exception.internal_server_error_exception import InternalServerErrorException

from api.v1.authors.controllers.authors_controller import authors_router
from api.v1.books.controllers.books_controller import books_router

library_management_api = NinjaAPI(
    title="Library Management API",
    description="Library Management API Documentation",
    version="3.0",
)

library_management_api.add_router("/authors", authors_router)
library_management_api.add_router("/books", books_router)


@library_management_api.exception_handler(BadRequestException)
def handle_bad_request_exception(request: HttpRequest, exc: BadRequestException):
    return library_management_api.create_response(request=request, status=400, data={
        "message": str(exc)
    })


@library_management_api.exception_handler(ForbiddenException)
def handle_forbidden_exception(request: HttpRequest, exc: ForbiddenException):
    return library_management_api.create_response(request=request, status=403, data={
        "message": str(exc)
    })


@library_management_api.exception_handler(NotFoundException)
def handle_not_found_exception(request: HttpRequest, exc: NotFoundException):
    return library_management_api.create_response(request=request, status=404, data={
        "message": str(exc)
    })


@library_management_api.exception_handler(InternalServerErrorException)
def handle_internal_server_error_exception(request: HttpRequest, exc: InternalServerErrorException):
    return library_management_api.create_response(request=request, status=500, data={
        "message": str(exc)
    })
