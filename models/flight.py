class Flight:
    def __init__(self, flight_number: str, airplane):
        self.flight_number = flight_number
        self.airplane = airplane
        self.passengers = []
        self.airplane.available = False

    def add_passenger(self, passenger):
        if len(self.passengers) < self.airplane.capacity:
            self.passengers.append(passenger)
            return True
        return False
    
    def __str__(self):
        return f"Flight {self.flight_number}: {len(self.passengers)}/\
        {self.airplane.capacity} passengers"
    