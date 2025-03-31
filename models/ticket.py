import random


class Ticket:

    # COMMON_ROUTES = [
    #     "NYC-LON", "LAX-SFO", "CHI-MIA", 
    #     "PAR-TOK", "BER-DXB", "SYD-SIN"
    # ]

    def __init__(self, direction: str):
        self.number = self._generate_number()
        self.direction = direction
        self.available = True

    def _generate_number(self) -> str:
        """Generate  ticket number"""
        return f"TK{random.randint(1000, 9999)}"
    
    def mark_used(self):
        """ ticket as used"""
        self.available = False
    
    def __str__(self):
        status = "AVAILABLE" if self.available else "USED"
        return f"Ticket {self.number} ({self.direction}) - {status}"