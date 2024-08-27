from api.v1.db.Authors import Authors
from api.v1.exception.internal_server_error_exception import InternalServerErrorException
from api.v1.exception.notfound_exception import NotFoundException
class AuthorsService:
    @staticmethod
    def create_author(name, bio, birth_date):
        try:
            author = Authors(name=name, bio=bio, birth_date=birth_date)
            author.save()

            author_data = {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "birth_date": author.birth_date
            }

            return author_data
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        

    @staticmethod
    def get_authors():
        try:
            authors = Authors.objects.all()
            
            authors_data = []
            for author in authors:
                author_data = {
                    "id": author.id,
                    "name": author.name,
                    "bio": author.bio,
                    "birth_date": author.birth_date
                }
                authors_data.append(author_data)

            return authors_data
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        
    @staticmethod
    def get_author_by_id(id):
        try:
            author = Authors.objects.get(id=id)
            author_data = {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "birth_date": author.birth_date
            }

            return author_data
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        
    @staticmethod
    def update_author_by_id(id, name, bio, birth_date):
        try:
            author = Authors.objects.get(id=id)
            author.name = name
            author.bio = bio
            author.birth_date = birth_date
            author.save()

            author_data = {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "birth_date": author.birth_date
            }

            return author_data
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        
    @staticmethod
    def delete_author_by_id(id):
        try:
            author = Authors.objects.get(id=id)
            author.delete()
            return
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException