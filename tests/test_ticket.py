import unittest
from models.ticket import Ticket

class TestTicket(unittest.TestCase):
    def test_ticket_creation(self):
        t = Ticket("PAR-TOK")
        self.assertTrue(t.available)
        
    def test_mark_used(self):
        t = Ticket("LON-NYC")
        t.mark_used()
        self.assertFalse(t.available)

if __name__ == '__main__':
    unittest.main()