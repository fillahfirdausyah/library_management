from ninja import Schema
from pydantic import validator

class BooksBodySchema(Schema):
    author: int
    title: str
    description: str
    publish_date: str

    @validator("publish_date")
    def validate_publish_date(cls, value):
        return value

class BooksGetByIdPathSchema(Schema):
    id: int

    @validator("id")
    def validate_id(cls, value):
        return value
    
