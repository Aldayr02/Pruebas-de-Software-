import hashlib
import json
import os
import secrets
import string
import unittest
from io import StringIO
from unittest.mock import patch

from .source_code import (
    generate_password_hash,
    generate_salt,
    load_user_data,
    login,
    register,
    save_user_data,
)


class TestGenerateSalt(unittest.TestCase):

    def test_salt_length(self):
        salt = generate_salt()
        self.assertEqual(len(salt), 32)

    def test_salt_type(self):

        salt = generate_salt()
        self.assertIsInstance(salt, str)


class TestGeneratePasswordHash(unittest.TestCase):

    def test_password_hash_output(self):
        password = "pwd"
        salt = "salt"
        expected_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        generated_hash = generate_password_hash(password, salt)
        self.assertEqual(generated_hash, expected_hash)

    def test_different_passwords_produce_different_hashes(self):
        salt = "salt"
        password1 = "pwd1"
        password2 = "pwd2"
        hash1 = generate_password_hash(password1, salt)
        hash2 = generate_password_hash(password2, salt)
        self.assertNotEqual(hash1, hash2)

    def test_different_salts_produce_different_hashes(self):
        password = "pwd"
        salt1 = "salt1"
        salt2 = "salt2"
        hash1 = generate_password_hash(password, salt1)
        hash2 = generate_password_hash(password, salt2)
        self.assertNotEqual(hash1, hash2)


class TestLoadUserData(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_user_data.json"
        self.test_data = {"user1": "data1"}
        with open(self.test_file, "w") as f:
            json.dump(self.test_data, f)

    def test_load_existing_user_data(self):
        user_data = load_user_data()
        self.assertEqual(user_data, self.test_data)

    def test_load_nonexistent_user_data(self):
        os.remove(self.test_file)
        user_data = load_user_data()
        self.assertEqual(user_data, {})


class TestSaveUserData(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_user_data.json"
        self.test_data = {"user1": "data1"}

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_user_data(self):
        global USER_DATA_FILE
        USER_DATA_FILE = self.test_file

        save_user_data(self.test_data)

        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, "r") as f:
            file_contents = json.load(f)
        self.assertEqual(file_contents, self.test_data)


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_user_data.json"
        self.test_data = {"Asthorias": "data1"}
        with open(self.test_file, "w") as f:
            json.dump(self.test_data, f)

    @patch("sys.stdout", new_callable=StringIO)
    def test_unsusccesful_register(self, mock):
        expected_output = "User already exists. Please choose a different username."

        register("Asthorias")
        self.assertEqual(mock.getvalue(), expected_output)


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_user_data.json"
        self.test_data = {"user1": "data1"}
        with open(self.test_file, "w") as f:
            json.dump(self.test_data, f)

    @patch("sys.stdout", new_callable=StringIO)
    def test_unsusccesful_register(self, mock):
        expected_output = "User does not exist. Please register first."

        login("Asthorias")
        self.assertEqual(mock.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
