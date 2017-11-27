import unittest
#include "week1_ex1_basic.py"

class TestMyMethods(unittest.TestCase):

    def test1stIsSmaller(self):
        self.assertEqual(combineStr('bye', 'goodmorning'), 'bgyoeodmorning')

    def testSameSize(self):
       self.assertEqual(combineStr('bye', 'hey'), 'bhyeyy')

    def test1stIsBigger(self):
       self.assertEqual(combineStr('goodmorning', 'hey'), 'ghoeoydmorning') 

if __name__ == '__main__':
    unittest.main()
