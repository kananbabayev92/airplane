import unittest
from models.airplane import Airplane

class TestAirplane(unittest.TestCase):
    def setup(self):
        # Create test airplane with 150 seats
        self.test_plane = Airplane("Boeing 737", 150)

    def test_airplane_creation(self):
        """Test airplane initializes correctly"""
        self.assertEqual(self.test_plane.model, "Boeing 737")
        self.assertEqual(self.test_plane.capacity, 150)

if __name__ == '__main__':
    unittest.main()