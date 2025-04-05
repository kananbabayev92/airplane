class Flight:
    """Represents an airline flight with passengers and aircraft.
    
    A Flight connects an airplane with passengers, managing boarding operations
    while tracking capacity constraints. Automatically marks the assigned
    airplane as unavailable when created.

    Attributes:
        flight_number (str): Unique identifier for the flight (e.g., "FL123")
        airplane (Airplane): Aircraft assigned to this flight
        passengers (list): List of Passenger objects on this flight
    """

    def __init__(self, flight_number: str, airplane):
        """Initializes a new flight with an aircraft.
        
        Args:
            flight_number: Unique flight identifier (e.g., "FL123")
            airplane: Airplane object assigned to this flight
            
        Note:
            Automatically marks the airplane as unavailable for other flights
        """
        self.flight_number = flight_number
        self.airplane = airplane
        self.passengers = []
        self.airplane.available = False

    def add_passenger(self, passenger) -> bool:
        """Attempts to add a passenger to the flight.
        
        Args:
            passenger: Passenger object to board
            
        Returns:
            bool: True if boarding was successful, False if flight is at capacity
            
        Example:
            >>> flight = Flight("FL123", airplane)
            >>> flight.add_passenger(passenger)
            True
        """
        if len(self.passengers) < self.airplane.capacity:
            self.passengers.append(passenger)
            return True
        return False
    
    def __str__(self) -> str:
        """Provides human-readable flight status.
        
        Returns:
            str: Flight summary including passenger count and capacity
            
        Example:
            >>> print(Flight("FL123", airplane))
            Flight FL123: 0/150 passengers
        """
        return f"Flight {self.flight_number}: {len(self.passengers)}/{self.airplane.capacity} passengers"
    