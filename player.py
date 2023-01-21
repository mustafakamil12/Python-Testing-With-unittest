import unittest

def myPlayer(x,y):
    return x / y

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.x = 20
        self.y = 4

    def test_run(self):
        result = myPlayer(self.x, self.y)
        self.assertTrue(result == 5)

    def test_attack(self):
        result = myPlayer(self.x, self.y)
        self.assertTrue(result == 5.75)

    def tearDown(self):
        print("\nEnd with myPlayer")