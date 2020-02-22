import unittest
import utilities

class TestIsStopWord(unittest.TestCase):
  def test_is_stop_word_true(self):
    self.assertTrue(utilities.is_stop_word('a'))
    self.assertTrue(utilities.is_stop_word('A'))
    self.assertTrue(utilities.is_stop_word('not'))
    self.assertTrue(utilities.is_stop_word('NOT'))
    self.assertTrue(utilities.is_stop_word('yourselves'))
    self.assertTrue(utilities.is_stop_word('YOURSELVES'))

  def test_is_stop_word_false(self):
    self.assertFalse(utilities.is_stop_word('apple'))
    self.assertFalse(utilities.is_stop_word('banana'))

if __name__ == '__main__':
  unittest.main()
