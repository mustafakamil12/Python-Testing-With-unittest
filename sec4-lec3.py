import unittest

class suiteTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20

    def testadd(self):
        """Add"""
        result = self.a+self.b
        self.assertTrue(result == 100)
    def testsub(self):
        """sub"""
        result = self.a-self.b
        self.assertTrue(result == -10)

def suite():
    suite = unittest.TestSuite()

    suite.addTest (suiteTest("testadd"))
    suite.addTest (suiteTest("testsub"))

    return suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)   # Set verbosity to 2 for more detailed output
   test_suite = suite()
   result = runner.run (test_suite)

   print ("---- START OF TEST RESULTS")
   print (result)

   print ("result::errors")
   print (result.errors)

   print ("result::failures")
   print (result.failures)

   print ("result::skipped")
   print (result.skipped)

   print ("result::successful")
   print (result.wasSuccessful())

   print ("result::test-run")
   print (result.testsRun)
   print ("---- END OF TEST RESULTS")
