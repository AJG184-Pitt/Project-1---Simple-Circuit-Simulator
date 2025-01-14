class resistor:
    def __init__(self, name, bus1, bus2, r, g):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = g

    @classmethod
    def calc_g(self):
        # Calcualtes the conductance of resistor
        self.g = 1 / self.r
