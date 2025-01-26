class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = self.calculate_resistance()
        self.g = self.calculate_conductance()
    
    def calculate_conductance(self):
        self.g = float
        if self.r == 0:
            return float('inf')
        
        print(f"g: {self.g} | r: {self.r}")
        self.g = 1 / self.r

    def calculate_resistance(self):
        self.r = float
        if self.p == 0:
            return float('inf')
        self.r = (self.v**2) / self.p
