import json
from django.test import TestCase
from ninja.testing import TestClient

from api.v1.authors.controllers.authors_controller import authors_router
from api.v1.db.Authors import Authors

class TestAuthors(TestCase):
    def setUp(self):
        self.client = TestClient(authors_router)
        self.author = Authors.objects.create(name="Test Author", bio="Test Author Bio", birth_date="2000-01-01")

    def test_create_author(self):
        response = self.client.post("", data=json.dumps({
            "name": "Test Author 2",
            "bio": "Test Author Bio 2",
            "birth_date": "2000-01-02"
        }), content_type="application/json")

        result = {
            'message': 'Author created successfully',
            'payload': {
                'id': 2,
                'name': 'Test Author 2',
                'bio': 'Test Author Bio 2',
                'birth_date': '2000-01-02'
            }
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), result)

    def test_get_authors(self):
        response = self.client.get("")

        self.assertEqual(response.status_code, 200)
        self.assertIn('payload', response.json())

    def test_get_author_by_id(self):
        author_id = self.author.id
        response = self.client.get(f"/{author_id}")

        self.assertEqual(response.status_code, 200)
        self.assertIn('payload', response.json())

    def test_update_author_by_id(self):
        author_id = self.author.id
        response = self.client.put(f"/{author_id}", data=json.dumps({
            "name": "Test Author 2",
            "bio": "Test Author Bio 2",
            "birth_date": "2000-01-02"
        }), content_type="application/json")

        result = {
            'message': 'Author updated successfully',
            'payload': {
                'id': author_id,
                'name': 'Test Author 2',
                'bio': 'Test Author Bio 2',
                'birth_date': '2000-01-02'
            }
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)

    def test_delete_author_by_id(self):
        author_id = self.author.id
        response = self.client.delete(f"/{author_id}")

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_get_books_by_author_id(self):
        author_id = self.author.id
        response = self.client.get(f"/{author_id}/books")

        self.assertEqual(response.status_code, 200)
        self.assertIn('payload', response.json())

    def tearDown(self):
        self.author.delete()


    
       