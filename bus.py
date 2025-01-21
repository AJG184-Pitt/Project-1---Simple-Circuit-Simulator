class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v = float

    def set_bus_voltage(self, voltage):
        self.v = voltage
