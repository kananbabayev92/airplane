import unittest

from models.baggage import Baggage
from models.flight import Flight
from models.airplane import Airplane


class TestBaggage(unittest.TestCase):
    def setUp(self):
        self.test_airplane = Airplane("TestJet", 2)
        self.test_baggage = Baggage(15.0, "FL132", "John Bakinec")
        self.test_flight = Flight("FL132", self.test_airplane)
    

    def test_baggage_creation(self):
        self.assertEqual(self.test_baggage.flight_number, "FL132")
        self.assertEqual(self.test_baggage.passenger_name, "John Bakinec")
        self.assertEqual(self.test_baggage.bag_weight, 15.0)


    def test_check_baggage(self):
        self.test_baggage.bag_weight = 15.0
        self.assertEqual(self.test_baggage.check_baggage(),"Baggage is within weight limit.")
        self.test_baggage.bag_weight = 25.0
        self.assertEqual(self.test_baggage.check_baggage(), "Baggage exceeds weight limit.")

if __name__ == "__main__":
    unittest.main()
