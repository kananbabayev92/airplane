import unittest
from models.passenger import Passenger
from models.ticket import Ticket

class TestPassenger(unittest.TestCase):
    def setUp(self):
        self.passenger = Passenger("John Doe", "P001")
        self.ticket = Ticket("NYC-LDN")

    def test_passenger_creation(self):
        self.assertEqual(self.passenger.name, "John Doe")
        self.assertEqual(self.passenger.passenger_id, "P001")
        self.assertEqual(len(self.passenger.tickets), 0)

    def test_add_ticket(self):
        self.passenger.add_ticket(self.ticket)
        self.assertEqual(len(self.passenger.tickets), 1)
        self.assertIsInstance(self.passenger.tickets[0], Ticket)

    def test_string_representation(self):
        self.assertEqual(str(self.passenger), "John Doe (ID: P001)")

if __name__ == '__main__':
    unittest.main()