import unittest

from greeter import greet, shout


class GreetTests(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Octocat"), "Hello, Octocat!")

    def test_defaults_to_world(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_blank_name_falls_back_to_world(self):
        self.assertEqual(greet("   "), "Hello, World!")

    def test_trims_whitespace(self):
        self.assertEqual(greet("  Mona  "), "Hello, Mona!")


class ShoutTests(unittest.TestCase):
    def test_shouts(self):
        self.assertEqual(shout("Octocat"), "HELLO, OCTOCAT!")


if __name__ == "__main__":
    unittest.main()
