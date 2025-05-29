import unittest

def add(x,y):
    return x + y

class SimpleTest(unittest.TestCase):        # Test case.
    def testadd1(self):                     # Test method.
        self.assertEqual(add(4,5),9)

if __name__ == '__main__':
    unittest.main()