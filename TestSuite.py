import unittest
from TestModule1 import TestPredictions
from TestModule2 import TestBMI
from TestModule3 import TestFindAge
from TestModule4 import TestHeightWeight

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPredictions))
    suite.addTest(unittest.makeSuite(TestBMI))
    suite.addTest(unittest.makeSuite(TestFindAge))
    suite.addTest(unittest.makeSuite(TestHeightWeight))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()