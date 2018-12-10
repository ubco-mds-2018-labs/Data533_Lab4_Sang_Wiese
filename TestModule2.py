import health.prediction.bodymassindex as bm
import health.prediction.predictparents as ph
import health.conversion.find_age as find
import health.conversion.metric_units as met
from health import athlete
import unittest

class TestBMI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self): # Setting up for the test
        self.p1 = athlete.Powerlifter('Egor', '1989-06-09',69,167,68,64)
        self.p2 = athlete.Swimmer('kim','1995-01-01',76,178,75,68)

    def tearDown(self):
        print('Tear Down')

    def test_bmi(self):
        #Use function inches_to_cm from module metric_units
        E_height = met.inches_to_cm(self.p1.height)
        K_height = met.inches_to_cm(self.p2.height)

        #Use function pounds_to_kg from module metric_units
        E_weight = met.pounds_to_kg(self.p1.weight)
        K_weight = met.pounds_to_kg(self.p2.weight)

        #Athlete must maintain their BMI to be greater than 20.1.
        self.assertIsNotNone(E_height)
        self.assertIsNotNone(K_height)
        self.assertIsNotNone(E_weight)
        self.assertIsNotNone(K_weight)
        self.assertGreaterEqual(bm.bmi(self.p1.name, E_height, E_weight),20.1)
        self.assertGreaterEqual(bm.bmi(self.p2.name, K_height, K_weight),20.1)

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

unittest.main(argv=[''], verbosity=2, exit=False)
