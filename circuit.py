from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource

class Circuit:
    def __init__(self, name, buses, resistors, loads):
        self.name = name
        self.buses = dict(buses)
        self.resistors = dict(resistors)
        self.loads = dict(loads)
        self.vsource = None
        self.i = 0.0

    def add_bus(self, name: str, v: float):
        bus_obj = Bus(name, v)
        self.buses[bus] = bus_obj
         
    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float, g: float):
        resistor_obj = Resistor(name, bus1, bus2, r, g)
        self.resistors[resistor] = resistor_obj

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        load_obj = Load(name, bus, p, v)
        self.loads[load] = load_obj

    def add_vsource_element(self, name: str, bus1: str, v: float):
        vsource_obj = Vsource(name, bus1, v)
        self.vsource = vsource_obj

    def set_i(self, current):
        self.i = float(current)

    def print_nodal_voltage(self):
        print(f"Nodal voltage for circuit {self.name}")

        for bus_name, bus in self.buses.items():
            print(f"Bus: {bus_name}, {bus}")

        if hasattr(self, 'vsource'):
            print(f"Vsource name: {self.vsource.name}")
            print(f"Vsource bus: {self.vsource.bus1}")
            print(f"Vsource voltage: {self.vsource.v}")

    def print_circuit_current(self):
        print(f"Current at circuit {self.name}")

        # Calculate the current based on resistance
        total_resistance = 0
        for resistor in self.resistors.values():
            total_resistance += resistor.r
        
        # If statement for printing current
        if total_resistance != 0:
            current  = self.vsource.v / total_resistance
            print(f"Calculated current {current}")
        else:
            print("Cannot calculate current due to zero resistance")
