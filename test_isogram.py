import unittest

from isogram import is_isogram

class IsIsogramTestCase(unittest.TestCase):
    def test_is_isogram(self):
        self.assertTrue(is_isogram("isogram"), "Single word with no repeating ")
        self.assertTrue(is_isogram("uncopyrightable"), "Long word with no repeated letter ")
        self.assertTrue(is_isogram("tea"), "Short word with no repeated letter")

        self.assertFalse(is_isogram("sets"), "Word with repeated letter 's'")
        self.assertFalse(is_isogram("tata"), "Word with repeated letter 't' and 'a'")

        self.assertTrue(is_isogram(" "), "Empty string is considered an isogram")

        self.assertTrue(is_isogram("x"), "Single character is considered an isogram")

if __name__ == '__main__':
    unittest.main()