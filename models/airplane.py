class Airplane:
    """Physical airplane parametres"""
    def __init__(self, model: str, capacity: int):
        self.model = model
        self.capacity = capacity

    def __str__(self):
        return f"Plane model:{self.model} - Capacity:{self.capacity}"
