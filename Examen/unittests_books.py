import unittest
from io import StringIO
from unittest.mock import patch

from .source_code_books import Book, BookStore


class TestBookClass(unittest.TestCase):

    def setUp(self):
        self.book = Book("Shadow Slave", "Asthorias", 1, 2)

    def test_initialization(self):
        self.assertEqual(self.book.title, "Shadow Slave")
        self.assertEqual(self.book.author, "Asthorias")
        self.assertEqual(self.book.price, 1)
        self.assertEqual(self.book.quantity, 2)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display(self, mock):
        expected_output = (
            "Title: Shadow Salve\n"
            "Author: Asthorias\n"
            "Price: $1.0\n"
            "Quantity: 2\n"
        )

        self.book.display()
        self.assertEqual(mock.getvalue(), expected_output)


class TestBookStoreClass(unittest.TestCase):
    def setUp(self):
        self.bookstore = BookStore()

    def test_initialization(self):
        self.assertEqual(self.bookstore, [])

    @patch("sys.stdout", new_callable=StringIO)
    def test_add_books(self, mock):
        expected_output = "Book  'Shadow Slave added to the store"

        self.bookstore.add_book(Book("Shadow Slave", "Asthorias", 1, 2))
        self.assertEqual(mock.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_books(self, mock):
        expected_output = (
            "Title: Shadow Salve\n"
            "Author: Asthorias\n"
            "Price: $1.0\n"
            "Quantity: 2\n"
        )

        self.bookstore.display_books()
        self.assertEqual(mock.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_book_valid(self, mock):
        expected_output = (
            "Title: Shadow Salve\n"
            "Author: Asthorias\n"
            "Price: $1.0\n"
            "Quantity: 2\n"
        )

        self.bookstore.search_book("Shadow Slave")
        self.assertEqual(mock.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_book_invalid(self, mock):
        expected_output = "No book found with title 'Inmortal Asura'."
        self.bookstore.search_book("Inmortal Asura")
        self.assertEqual(mock.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
