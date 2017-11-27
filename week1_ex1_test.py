from week1_ex1_basic import *
import unittest

class TestMyMethods(unittest.TestCase):

    def test1stIsSmaller(self):
        self.assertEqual(combineStr('bye', 'goodmorning'), 'bgyoeodmorning')

    def testSameSize(self):
       self.assertEqual(combineStr('bye', 'hey'), 'bhyeey')

    def test1stIsBigger(self):
       self.assertEqual(combineStr('goodmorning', 'hey'), 'ghoeoydmorning')
    
    def testNotString(self):
        with self.assertRaises(TypeError):
            combineStr(123, [45])

unittest.main()