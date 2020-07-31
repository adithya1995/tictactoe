import unittest
from calc import add,mult

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4,3),7)

    def test_mult(self):
        self.assertEqual(mult(3,4),12)

    def test_random(self):
        self.assertFalse(False)
        
    def test_true(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
