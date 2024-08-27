from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.errors import AuthenticationError, ValidationError

from api.v1.authors.controllers.authors_controller import authors_router

library_management_api = NinjaAPI(
    title="Library Management API",
    description="Library Management API Documentation",
    version="3.0",
)

library_management_api.add_router("/authors", authors_router)

