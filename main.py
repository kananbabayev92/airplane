import numpy as nm

from logging_config import setup_logging
from models.airplane import Airplane
from models.passenger import Passenger 
from models.flight import Flight
from models.ticket import Ticket
from models.baggage import Baggage
from random import uniform


def main():
    setup_logging()
    
    # Create resources
    plane = Airplane("Boeing 737", 5)

    passengers = [
        Passenger("Alex", "P001"),
        Passenger("Kanan", "P002"),
        Passenger("Alim", "P003"),
        Passenger("Qasim", "P004"), 
        Passenger("Yetim", "P005")  
    ]
    
    # Create flight
    flight = Flight("FL123", plane)

    # Add baggage
    for passenger in passengers:
        bag = Baggage(round(uniform(15.0, 25.0), 1), flight.flight_number, passenger.name) 
        baggage_status = bag.check_baggage()
        if bag.bag_weight > 20:
            baggage_fee = bag.calculate_fee()
            print(f"{passenger.name} 's baggege status:{baggage_status} with fee:{round(baggage_fee, 2)}$")
        else:
            print(f"{passenger.name} 's baggege status:{baggage_status}")
        
        
    # Board passengers
    for i, passenger in enumerate(passengers[:5]): 
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