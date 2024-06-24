import unittest

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

class Test1(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(4,5),9)
    def testadd2(self):
        self.assertEqual(add(1,3),7)
    def testadd3(self):
        self.assertEqual(add(4,2),6)

class Test2(unittest.TestCase):
    def testsub1(self):
        self.assertEqual(sub(9,3),6)
    def testsub2(self):
        self.assertEqual(sub(9,2),6)
    def testsub3(self):
        self.assertEqual(sub(1,2),5)

testCases = [Test1,Test2]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testCases:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)