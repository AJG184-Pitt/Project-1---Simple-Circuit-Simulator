class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = 0.0
        self.g = 0.0

    def calculate_g(self):
        if self.v <= 0:
            self.v = 0.0

        # Calculate conductance of load
        self.r = self.v**2 / self.p
        self.g = 1 / self.r
