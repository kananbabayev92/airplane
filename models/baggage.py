class Baggage:
    def __init__(self, bag_weight: float, flight_number: str, passenger_name: str):
        self.passenger_name = passenger_name 
        self.bag_weight = bag_weight
        self.flight_number = flight_number

    def check_baggage(self):
        if self.bag_weight > 20:
            return "Baggage exceeds weight limit."
        else:
            return "Baggage is within weight limit."
        
    def calculate_fee(self,):
        if  self.bag_weight > 20:
            excess_weight = self.bag_weight - 20.0
            fee = excess_weight * 10.0
            return fee
        return 0.0
         