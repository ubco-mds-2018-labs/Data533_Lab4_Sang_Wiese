import health.conversion.find_age as find

from health import athlete

import unittest

class TestFindAge(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
              
    def setUp(self): # Setting up for the test
        self.p1 = athlete.Powerlifter('Egor', '1989-06-09',69,167,68,64)
        self.p2 = athlete.Swimmer('kim','1987-12-29',76,178,75,68)
        self.p3 = athlete.Swimmer('Shelly','29-01-1990',76,178,75,68)      
    
    def tearDown(self):
        print('Tear Down')
    
    def test_find_age(self):
        E_age = find.year_to_age(self.p1.name, self.p1.DOB)
        K_age = find.year_to_age(self.p2.name, self.p2.DOB)
        S_age = find.year_to_age(self.p3.name, self.p3.DOB)

        self.assertEqual(E_age, 29)
        self.assertEqual(K_age, 30)
        self.assertNotEqual(E_age, K_age)
        self.assertIsNotNone(E_age)
        self.assertIsNotNone(K_age)
        
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

unittest.main(argv=[''], verbosity=2, exit=False)
