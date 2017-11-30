from week3_ex1_basic import *
import unittest

class TestMyMethods(unittest.TestCase):

    def testStringHasOneWord(self):
        self.assertEqual(mirrorWords(['hello'], []), 'olleh')

    def testManyWords(self):
       self.assertEqual(mirrorWords(['bye', 'maria'], []), 'eyb airam')

    def testStringEmpty(self):
       self.assertEqual(mirrorWords([], []), '')

unittest.main()