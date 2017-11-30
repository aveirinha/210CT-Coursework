from week3_ex2_basic import *
import unittest

class TestMyMethods(unittest.TestCase):

    def testListIsEmpty(self):
        self.assertFalse(linearSearch([], 4))
   
    def testValueNotInList(self):
       self.assertFalse(linearSearch([1, 2, 3, 4], 7))

    def testValueInTheListLast(self):
       self.assertTrue(linearSearch([1, 2, 3, 4], 4))

    def testValueInTheList1st(self):
       self.assertTrue(linearSearch([1, 2, 3, 4], 1))

    def testValueInTheListMiddle(self):
       self.assertTrue(linearSearch([1, 2, 3, 4, 5, 6], 4))    

unittest.main()