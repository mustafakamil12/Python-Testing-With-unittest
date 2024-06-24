import unittest

def div(a,b):
   return a/b
class raiseTest(unittest.TestCase):
   def testraise(self):
      self.assertRaises(ZeroDivisionError, div, 1,1)

if __name__ == '__main__':
   unittest.main()