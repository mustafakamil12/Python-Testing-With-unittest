import unittest

def myScenario(x,y):
    return x + y

class TestScenario(unittest.TestCase):

    def setUp(self):
        self.x = 10
        self.y = 20

    def test_run(self):
        result = myScenario(self.x, self.y)
        self.assertTrue(result == 30)

    def test_attack(self):
        result = myScenario(self.x, self.y)
        self.assertTrue(result == 70)

    def tearDown(self):
        print("\nEnd with myScenario")