import unittest
import time
import timeout_decorator

class timeoutTest(unittest.TestCase):

   @timeout_decorator.timeout(5)
   def testtimeout(self):
      print("Start")
   for i in range(1,10):
      time.sleep(1)
      print("%d seconds have passed" % i)
      
if __name__ == '__main__':
   unittest.main()