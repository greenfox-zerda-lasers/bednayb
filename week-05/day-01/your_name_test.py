#TEST THE FUNCTIONS


import unittest
import your_name_work

class PrimesTestCase(unittest.TestCase):
    """Tests for `isAnagram.py`."""

    def test_anagram(self):

        self.assertTrue(your_name_work.anagramm("Alma","ma la"))
        self.assertTrue(your_name_work.anagramm("Alma","ma la"))



    # """Tests for `count_letters.py`."""
    def test_count_letters(self):

        self.assertEqual(your_name_work.count_letters("almafa"),{'f': 1, 'a': 3, 'l': 1, 'm': 1})

if __name__ == '__main__':
    unittest.main()
