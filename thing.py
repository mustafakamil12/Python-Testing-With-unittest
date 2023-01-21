import unittest

def myThing(x,y):
    return x ** y

class TestThing(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 4

    def test_run(self):
        result = myThing(self.x, self.y)
        self.assertTrue(result == 32)

    def test_attack(self):
        result = myThing(self.x, self.y)
        self.assertTrue(result == 64)

    def tearDown(self):
        print("\nEnd with myThing")