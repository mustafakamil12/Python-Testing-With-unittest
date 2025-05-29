import unittest

class TestFixtures(unittest.TestCase):
    #it will run before any test.
    @classmethod
    def setUpClass(cls):
        print ('\nsetUpClass() --> called once before any tests in class')

    #it will be run after all tests.
    @classmethod
    def tearDownClass(cls):
        print ('\ntearDownClass() --> called once after all tests in class')

    def setUp(self):
        print("")
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        print ("\ncalling setUp() method for --> ",name)
    def tearDown(self):
        print ('\nend of test',"using tearDown() --> ",self.shortDescription())

    def test1(self):
        """One"""
        print("start test1")
        result = self.a+self.b
        self.assertTrue(True)   # result == 10
    def test2(self):
        """Two"""
        print("start test2")
        result = self.a-self.b
        self.assertTrue(False)  # result == 10

if __name__ == '__main__':
    unittest.main()
