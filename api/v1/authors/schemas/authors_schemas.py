from ninja import Schema
from pydantic import validator

class AuthorsBodySchema(Schema):
    name: str
    bio: str
    birth_date: str

    @validator('birth_date')
    def validate_birth_date(cls, value):
        return value
    
class AuthorsGetByIdPathSchema(Schema):
    id: int

    @validator('id')
    def validate_id(cls, value):
        return value