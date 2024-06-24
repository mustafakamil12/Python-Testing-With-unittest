import unittest

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

class SimpleTest2(unittest.TestCase):
    def setUp(self):        #Test fixture
        self.a = 10
        self.b = 20
        name = self.shortDescription()

        if name == "Add":
            self.a = 10
            self.b = 20
            print(name, self.a, self.b)

        if name == "Sub":
            self.a = 50
            self.b = 60
            print(name, self.a, self.b)

    def tearDown(self):
        print('end of test', self.shortDescription(),'\n')

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertTrue(result == 100)


    def testsub(self):
        """Sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)
     



if __name__ == '__main__':
    unittest.main()
