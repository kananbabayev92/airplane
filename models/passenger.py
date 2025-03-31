class Passenger:
    def __init__(self, name: str, passenger_id: str):
        self.name = name
        self.passenger_id = passenger_id
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def __str__(self):
        return f"{self.name} (ID: {self.passenger_id})"