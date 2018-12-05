import health.prediction.bodymassindex as bm
import health.prediction.predictparents as ph
import health.conversion.find_age as find
import health.conversion.metric_units as met
from health import athlete
import unittest

class TestPredictions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self): # Setting up for the test
        self.p1 = athlete.Powerlifter('Egor', '1989-06-09',69,167,68,64)
        self.p2 = athlete.Swimmer('kim','1995-01-01',76,178,75,68)

    def tearDown(self):
        print('Tear Down')

    def test_predictedheight(self):
        E_height = met.inches_to_cm(self.p1.height)
        K_height = met.inches_to_cm(self.p2.height)
        Fa_heightE = met.inches_to_cm(self.p1.fatherheight)
        Ma_heightE = met.inches_to_cm(self.p1.motherheight)
        Fa_heightK = met.inches_to_cm(self.p2.fatherheight)
        Ma_heightK = met.inches_to_cm(self.p2.motherheight)

        self.assertGreaterEqual(E_height, ph.Predicted_height(self.p1.name,Fa_heightE,Ma_heightE))
        self.assertGreaterEqual(K_height, ph.Predicted_height(self.p2.name,Fa_heightK,Ma_heightK))
        self.assertIsNotNone(Fa_heightE)
        self.assertIsNotNone(Ma_heightE)
        self.assertIsNotNone(Fa_heightK)
        self.assertIsNotNone(Ma_heightK)

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

unittest.main(argv=[''], verbosity=2, exit=False)
