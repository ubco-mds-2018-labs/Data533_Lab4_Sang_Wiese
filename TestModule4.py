import health.conversion.metric_units as met

from health import athlete

import unittest

class TestHeightWeight(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
              
    def setUp(self): # Setting up for the test
        self.p1 = athlete.Powerlifter('Egor', '1989-06-09',69,167,68,64)
        self.p2 = athlete.Swimmer('kim','1987-04-01',76,178,75,68)
              
    def tearDown(self):
        print('Tear Down')
    
    def test_height(self):
        E_height = met.inches_to_cm(self.p1.height)
        K_height = met.inches_to_cm(self.p2.height)

        self.assertEqual(E_height, 175.26)
        self.assertEqual(K_height, 193.04)
        self.assertNotEqual(E_height, K_height) #Check that the two are not equal
        self.assertGreater(E_height, self.p1.height) #Check that height measured in cenitmeters is a larger number than height measured in inches
        self.assertGreater(K_height, self.p2.height)  
        
        
    def test_weight(self):
        E_weight = met.pounds_to_kg(self.p1.weight)
        K_weight = met.pounds_to_kg(self.p2.weight)

        self.assertEqual(E_weight, 75.749864)
        self.assertEqual(K_weight, 80.739376)
        self.assertNotEqual(E_weight, K_weight) #Check that the two are not equal
        self.assertLess(E_weight,self.p1.weight) #Check that weight in kgs is a smaller number than weight in pounds
        self.assertLess(K_weight,self.p2.weight) #Check that weight in kgs is a smaller number than weight in pounds
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

unittest.main(argv=[''], verbosity=2, exit=False)