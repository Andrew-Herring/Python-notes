import unittest
# import sys
# sys.path.append('../')
# from palindrome import Palindrome


# logic

class Palindrome():
  def is_palindrome(self, source_string):

    # when the test runs, remove the spaces and force all the letters to be lower case
    source_stripped = "".join(source_string.split()).lower()
    # reverse the letters
    reverse_string = source_stripped[::-1]
    return source_stripped == reverse_string


# test

class PalindromeTest(unittest.TestCase):

  def test_is_palindrome(self):
    pal = Palindrome();
    # simple palindrome
    self.assertTrue(pal.is_palindrome("mom"))
    # palindrome with spaces
    self.assertTrue(pal.is_palindrome("race car"))
    # palindrome with spaces and upper case letters
    self.assertTrue(pal.is_palindrome("A Butt Tuba"))

if __name__=='__main__':
  unittest.main()