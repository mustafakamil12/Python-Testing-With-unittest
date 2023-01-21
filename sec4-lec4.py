import unittest

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

class Test1(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(4,5),9)
    def testadd2(self):
        self.assertEqual(add(4,5),10)
    def testadd3(self):
        self.assertEqual(add(4,5),0)


class Test2(unittest.TestCase):
    def testsub1(self):
        self.assertEqual(sub(4,5),9)
    def testsub2(self):
        self.assertEqual(sub(4,5),-1)
    def testsub3(self):
        self.assertEqual(sub(4,5),3)


testList = [Test1, Test2]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)
