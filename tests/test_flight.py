import unittest
from models.airplane import Airplane
from models.flight import Flight

class TestFlight(unittest.TestCase):
    def setUp(self):
        self.test_airplane = Airplane("TestJet", 2)
        
        # Create test flight
        self.test_flight = Flight("TEST123", self.test_airplane)

    def test_flight_creation(self):
        """Test flight initializes correctly"""
        self.assertEqual(self.test_flight.flight_number, "TEST123")
        self.assertEqual(self.test_flight.airplane.capacity, 2)
        self.assertEqual(len(self.test_flight.passengers), 0)

    def test_add_passenger(self):
        """Test passenger boarding within capacity"""
        # First passenger boards successfully
        self.assertTrue(self.test_flight.add_passenger("Passenger1"))
        self.assertEqual(len(self.test_flight.passengers), 1)
        
        # Second passenger boards successfully
        self.assertTrue(self.test_flight.add_passenger("Passenger2"))
        self.assertEqual(len(self.test_flight.passengers), 2)
        
        # Third passenger should be rejected (over capacity)
        self.assertFalse(self.test_flight.add_passenger("Passenger3"))
        self.assertEqual(len(self.test_flight.passengers), 2) 

if __name__ == '__main__':
    unittest.main()