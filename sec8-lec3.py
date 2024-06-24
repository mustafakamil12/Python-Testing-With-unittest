import unittest
import re

def callFun(x, y):
    myInteger = x
    myString = y
    myResult = myInteger + myString
    return myResult

class raiseTest(unittest.TestCase):
    def testraiseRegex(self):
        
        self.assertRaisesRegex(TypeError, "unsupported operand", callFun, 5,"TutorialsPoint")
      
if __name__ == '__main__':
   unittest.main()