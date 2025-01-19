class Resistor:
    def __init__(self, name: str, bus1: str, bus2: str, r: float, g: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = g

    def calc_g(self):
        # Calculates the conductance of resistor
        self.g = 1 / self.r
