class Bus:
    def __init__(self, name: str, v: float):
        self.name = name
        self.v = v

    def set_bus_voltage(self, voltage):
        self.v = voltage
