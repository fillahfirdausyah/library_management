import json
from django.test import TestCase
from ninja.testing import TestClient

from api.v1.books.controllers.books_controller import books_router
from api.v1.db.Authors import Authors
from api.v1.db.Books import Books

class TestBooks(TestCase):
    def setUp(self):
        self.client = TestClient(books_router)
        self.author = Authors.objects.create(name="Test Author", bio="Test Author Bio", birth_date="2000-01-01")
        self.book = Books.objects.create(author=self.author, title="Test Book", description="Test Book Description", publish_date="2022-01-01")

    def test_create_book(self):
        response = self.client.post("", data=json.dumps({
            "author": self.author.id,
            "title": "Test Book 2",
            "description": "Test Book Description 2",
            "publish_date": "2022-01-02"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())

    def test_get_books(self):
        response = self.client.get("")

        self.assertEqual(response.status_code, 200)
        self.assertIn('payload', response.json())

    def test_get_book_by_id(self):
        book_id = self.book.id
        response = self.client.get(f"/{book_id}")

        self.assertEqual(response.status_code, 200)
        self.assertIn('payload', response.json())

    def test_update_book_by_id(self):
        book_id = self.book.id
        response = self.client.put(f"/{book_id}", data=json.dumps({
            "author": self.author.id,
            "title": "Test Book 2",
            "description": "Test Book Description 2",
            "publish_date": "2022-01-02"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def tearDown(self):
        self.book.delete()
        self.author.delete()