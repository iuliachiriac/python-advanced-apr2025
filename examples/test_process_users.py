import json
import unittest

from process_users import get_users


class GetUsersTestCase(unittest.TestCase):
    def test_nonexistent_file(self):
        users = get_users("nonexistent.txt")
        self.assertIsInstance(users, list)
        self.assertEqual(0, len(users))

    def test_empty_file(self):
        open("empty.txt", "w").close()
        with self.assertRaises(json.JSONDecodeError):
            get_users("empty.txt")

    def test_invalid_json_file(self):
        with open("invalid_json.txt", "w") as f:
            f.write("test")
        with self.assertRaises(json.JSONDecodeError):
            get_users("empty.txt")

    def test_valid_json(self):
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
                "age": 32
            },
        ]
        with open("users.json", "w") as f:
            json.dump(users_expected, f)

        users_actual = get_users("users.json")

        self.assertIsInstance(users_actual, list)
        self.assertEqual(3, len(users_actual))
        self.assertIn(users_expected[0], users_actual)

    def test_valid_json_with_filtering(self):
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
        with open("users.json", "w") as f:
            json.dump(users_expected, f)

        users_actual = get_users("users.json", age_min=30, age_max=40)

        self.assertIsInstance(users_actual, list)
        self.assertEqual(1, len(users_actual))
        self.assertNotIn(users_expected[0], users_actual)
        self.assertNotIn(users_expected[2], users_actual)
        self.assertIn(users_expected[1], users_actual)
