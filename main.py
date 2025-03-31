from logging_config import setup_logging
from models.airplane import Airplane
from models.passenger import Passenger 
from models.flight import Flight
from models.ticket import Ticket

def main():
    setup_logging()
    
    # Create resources
    plane = Airplane("Boeing 737", 3)

    passengers = [
        Passenger("Alex", "P001"),
        Passenger("Kanan", "P002"),
        Passenger("Alim", "P003"),
        Passenger("Qasim", "P004"), 
        Passenger("Yetim", "P005")  
    ]
    
    # Create flight
    flight = Flight("FL123", plane)
    
    # Board passengers
    for i, passenger in enumerate(passengers[:3]): 
        if flight.add_passenger(passenger):
            ticket = Ticket(f"NYC-LDN-{i+1}") 
            passenger.add_ticket(ticket)
            ticket.mark_used()
            print(f"Boarded {passenger.name} with ticket {ticket.number}")
        else:
            print(f"Failed to board {passenger.name} (flight full)")
    
    # Display info
    print("\nFlight Status:", flight)
    print("\nPassenger Details:")
    for passenger in passengers:
        ticket_count = len(passenger.tickets)
        print(f"- {passenger.name}: {ticket_count} ticket(s)")
        if ticket_count > 0:
            print(f"  Last ticket: {passenger.tickets[-1]}")

if __name__ == "__main__":
    main()