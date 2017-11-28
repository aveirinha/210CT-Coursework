import unittest
from week1_ex2_basic import *

class TestMyMethods(unittest.TestCase):

    def testIsArmstrong(self):
        self.assertEqual(isArmstrong(371), 'Yes')

    def test2IsArmstrong(self):
        self.assertEqual(isArmstrong(370), 'Yes')

    def test3IsArmstrong(self):
        self.assertEqual(isArmstrong(153), 'Yes')
        
    def testIsNOTArmstrong(self):
        self.assertEqual(isArmstrong(254), 'No')

    def test2IsNOTArmstrong(self):
        self.assertEqual(isArmstrong(678), 'No')
                                
unittest.main()
