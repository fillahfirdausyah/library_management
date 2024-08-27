from api.v1.db.Authors import Authors
from api.v1.db.Books import Books
from api.v1.exception.internal_server_error_exception import InternalServerErrorException
from api.v1.exception.notfound_exception import NotFoundException

class BooksService:
    @staticmethod
    def get_books():
        try:
            books = Books.objects.all()
            
            books_data = []
            for book in books:
                book_data = {
                    "id": book.id,
                    "author": book.author.name,
                    "title": book.title,
                    "description": book.description,
                    "publish_date": book.publish_date
                }
                books_data.append(book_data)

            return books_data
        except Exception as e:
            print(e)
            raise InternalServerErrorException

    @staticmethod
    def get_book_by_id(id):
        try:
            book = Books.objects.get(id=id)
            book_data = {
                "id": book.id,
                "author": book.author.name,
                "title": book.title,
                "description": book.description,
                "publish_date": book.publish_date
            }

            return book_data
        except Books.DoesNotExist:
            raise NotFoundException(message="Book not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        
    @staticmethod
    def create_book(author_id, title, description, publish_date):
        try:
            author = Authors.objects.get(id=author_id)
            book = Books(author=author, title=title, description=description, publish_date=publish_date)
            book.save()

            book_data = {
                "id": book.id,
                "author": book.author.name,
                "title": book.title,
                "description": book.description,
                "publish_date": book.publish_date
            }

            return book_data
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException

    @staticmethod
    def update_book_by_id(id, author_id, title, description, publish_date):
        try:
            author = Authors.objects.get(id=author_id)
            book = Books.objects.get(id=id)
            book.author = author
            book.title = title
            book.description = description
            book.publish_date = publish_date
            book.save()

            book_data = {
                "id": book.id,
                "author": book.author.name,
                "title": book.title,
                "description": book.description,
                "publish_date": book.publish_date
            }

            return book_data
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Books.DoesNotExist:
            raise NotFoundException(message="Book not found")
        except Exception as e:
            print(e)

    @staticmethod
    def delete_book_by_id(id):
        try:
            book = Books.objects.get(id=id)
            book.delete()
            return
        except Books.DoesNotExist:
            raise NotFoundException(message="Book not found")
        except Exception as e:
            print(e)