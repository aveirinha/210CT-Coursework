import unittest

class TestMyMethods(unittest.TestCase):

    def test1stIsSmaller(self):
        self.assertEqual(combineStr('bye', 'goodmorning'), 'bgyoeodmorning')

    def testSameSize(self):
       self.assertEqual(combineStr('bye', 'hey'), 'bhyeyy')

    def test1stIsBigger(self):
       self.assertEqual(combineStr('goodmorning', 'hey'), 'ghoeoydmorning')

tester = TestMyMethods()
tester.test1stIsSmaller()

if __name__ == '__main__':
    unittest.main()
