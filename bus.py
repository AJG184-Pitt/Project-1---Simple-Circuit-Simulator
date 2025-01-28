class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v = 0.0

    def set_bus_voltage(self, voltage):
        self.v = float(voltage)
