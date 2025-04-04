import json
import os
import unittest

from process_users import get_users, get_name_age


class GetUsersTestCase(unittest.TestCase):
    users_expected = [
        {
            "email": "martha.foster@example.com",
            "age": 42
        },
        {
            "first_name": "Arthur",
            "last_name": "Fox",
            "age": 34
        },
        {
            "name": "Josh Kennedy",
            "age": 27
        },
    ]

    @classmethod
    def setUpClass(cls):
        open("empty.txt", "w").close()

        with open("invalid_json.txt", "w") as f:
            f.write("test")

        with open("users.json", "w") as f:
            json.dump(cls.users_expected, f)

    @classmethod
    def tearDownClass(cls):
        os.remove("empty.txt")
        os.remove("invalid_json.txt")
        os.remove("users.json")

    def test_nonexistent_file(self):
        users = get_users("nonexistent.txt")
        self.assertIsInstance(users, list)
        self.assertEqual(0, len(users))

    def test_empty_file(self):
        with self.assertRaises(json.JSONDecodeError):
            get_users("empty.txt")

    def test_invalid_json_file(self):
        with self.assertRaises(json.JSONDecodeError):
            get_users("invalid_json.txt")

    def test_valid_json(self):
        users_actual = get_users("users.json")

        self.assertIsInstance(users_actual, list)
        self.assertEqual(3, len(users_actual))
        self.assertIn(self.users_expected[0], users_actual)

    def test_valid_json_with_filtering(self):
        users_actual = get_users("users.json", age_min=30, age_max=40)

        self.assertIsInstance(users_actual, list)
        self.assertEqual(1, len(users_actual))
        self.assertNotIn(self.users_expected[0], users_actual)
        self.assertNotIn(self.users_expected[2], users_actual)
        self.assertIn(self.users_expected[1], users_actual)


class GetNameAgeTestCase(unittest.TestCase):
    def test_missing_name(self):
        user = {}
        with self.assertRaises(ValueError):
            get_name_age(user)

    def test_extract_name(self):
        users = [
            {
                "first_name": "Arthur",
                "last_name": "Fox",
                "age": 34
            },
            {
                "name": "Josh Kennedy",
                "age": 27
            },
        ]
        expected_names = ["Arthur Fox", "Josh Kennedy"]

        for user, expected_name in zip(users, expected_names):
            with self.subTest(f"Test failed for user = {user}"):
                name, age = get_name_age(user)
                self.assertEqual(expected_name, name)
                self.assertEqual(user["age"], age)
