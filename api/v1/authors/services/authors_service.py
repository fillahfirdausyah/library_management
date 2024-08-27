from api.v1.db.Authors import Authors
from api.v1.db.Books import Books
from api.v1.exception.internal_server_error_exception import InternalServerErrorException
from api.v1.exception.notfound_exception import NotFoundException
class AuthorsService:
    @staticmethod
    def create_author(name, bio, birth_date):
        """
        Creates a new author with the given name, bio, and birth date.
        
        Args:
            name (str): The name of the author.
            bio (str): The bio of the author.
            birth_date (str): The birth date of the author.
        
        Returns:
            dict: A dictionary containing the id, name, bio, and birth date of the created author.
        
        Raises:
            InternalServerErrorException: If an error occurs during the creation of the author.
        """
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
        """
        Retrieves a list of all authors in the database.
        
        Returns:
            list: A list of dictionaries containing the id, name, bio, and birth date of each author.
        
        Raises:
            InternalServerErrorException: If an error occurs during the retrieval of authors.
        """
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
        """
        Retrieves an author by their ID from the database.
        
        Args:
            id (int): The ID of the author to retrieve.
        
        Returns:
            dict: A dictionary containing the id, name, bio, and birth date of the author.
        
        Raises:
            NotFoundException: If the author with the given ID does not exist.
            InternalServerErrorException: If an error occurs during the retrieval of the author.
        """
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
        """
        Updates an author's information in the database.

        Args:
            id (int): The ID of the author to update.
            name (str): The new name of the author.
            bio (str): The new bio of the author.
            birth_date (str): The new birth date of the author.

        Returns:
            dict: A dictionary containing the updated author information.

        Raises:
            NotFoundException: If the author with the given ID does not exist.
            InternalServerErrorException: If an error occurs during the update.
        """
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
        """
        Deletes an author by their ID from the database.

        Args:
            id (int): The ID of the author to delete.

        Returns:
            None

        Raises:
            NotFoundException: If the author with the given ID does not exist.
            InternalServerErrorException: If an error occurs during the deletion.
        """
        try:
            author = Authors.objects.get(id=id)
            author.delete()
            return
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException
        
    @staticmethod
    def get_books_by_author_id(id):
        """
        Retrieves a list of books written by an author with the given ID.

        Args:
            id (int): The ID of the author.

        Returns:
            list: A list of dictionaries containing book data, including ID, author name, title, description, and publish date.

        Raises:
            NotFoundException: If the author with the given ID does not exist.
            InternalServerErrorException: If an error occurs during the retrieval.
        """
        try:
            author = Authors.objects.get(id=id)
            books = Books.objects.filter(author=author)
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
        except Authors.DoesNotExist:
            raise NotFoundException(message="Author not found")
        except Exception as e:
            print(e)
            raise InternalServerErrorException