# Palindrome test

class Palindrome():
  def is_palindrome(self, source_string):
    # Need more code to handle all the tests we threw at it.  Try your hand at making them pass

    source_stripped = "".join(source_string.split()).lower()
    reverse_string = source_stripped[::-1]
    # print(reverse_string)
    return source_string == reverse_string