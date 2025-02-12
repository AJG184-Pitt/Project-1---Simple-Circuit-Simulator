class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = self.calculate_resistance()
        self.g = self.calculate_conductance()
    
    def calculate_conductance(self):
        if self.r == 0:
            return float('inf')
        else:
            self.g = self.p / self.v**2
        return self.g

    def calculate_resistance(self):
        if self.p == 0:
            return float('inf')
        else:
            self.r = (self.v**2) / self.p
        return self.r
