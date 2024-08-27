from api.v1.db.Authors import Authors
from api.v1.db.Books import Books
from api.v1.exception.internal_server_error_exception import InternalServerErrorException
from api.v1.exception.notfound_exception import NotFoundException

class BooksService:
    @staticmethod
    def get_books():
        """
        Retrieves a list of all books from the database.

        Returns:
            list: A list of dictionaries containing book data, including ID, author name, title, description, and publish date.

        Raises:
            InternalServerErrorException: If an error occurs during the retrieval.
        """
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
        """
        Retrieves a book from the database by its ID.

        Args:
            id (int): The ID of the book to be retrieved.

        Returns:
            dict: A dictionary containing the book's data, including ID, author name, title, description, and publish date.

        Raises:
            NotFoundException: If the book with the specified ID does not exist.
            InternalServerErrorException: If an error occurs during the retrieval.
        """
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
        """
        Creates a new book in the database.

        Args:
            author_id (int): The ID of the author of the book.
            title (str): The title of the book.
            description (str): The description of the book.
            publish_date (date): The publication date of the book.

        Returns:
            dict: A dictionary containing the book's data, including ID, author name, title, description, and publish date.

        Raises:
            NotFoundException: If the author with the specified ID does not exist.
            InternalServerErrorException: If an error occurs during the creation.
        """
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
        """
        Updates a book in the database by its ID.

        Args:
            id (int): The ID of the book to update.
            author_id (int): The ID of the author of the book.
            title (str): The new title of the book.
            description (str): The new description of the book.
            publish_date (date): The new publication date of the book.

        Returns:
            dict: A dictionary containing the updated book's data, including ID, author name, title, description, and publish date.

        Raises:
            NotFoundException: If the author or book with the specified ID does not exist.
        """
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
        """
        Deletes a book from the database by its ID.

        Args:
            id (int): The ID of the book to delete.

        Returns:
            None

        Raises:
            NotFoundException: If the book with the specified ID does not exist.
            Exception: If an error occurs during deletion.
        """
        try:
            book = Books.objects.get(id=id)
            book.delete()
            return
        except Books.DoesNotExist:
            raise NotFoundException(message="Book not found")
        except Exception as e:
            print(e)