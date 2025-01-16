class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = float
        self.g = float

    def calculate_g(self):
        # Calculate conductance of load
        self.r = self.v / (self.p / self.v)
        self.g = 1 / self.r
