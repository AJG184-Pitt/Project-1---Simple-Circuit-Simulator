from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource

class Circuit:
    def __init__(self, name, buses, resistors, loads, vsource, i):
        self.name = name
        self.buses = dict(buses)
        self.resistors = dict(resistors)
        self.loads = dict(loads)
        self.vsource = vsource
        self.i = i

    def add_bus(self, name, v):
        bus = Bus(name, v)
        self.buses[name] = bus
         
    def add_resistor_element(self, name, bus1, bus2, r, g):
        resistor = Resistor(name, bus1, bus2, r, g)
        self.resistors[name] = resistor        

    def add_load_element(self, name, bus, p, q, g):
        load = Load(name, bus, p, q, g)
        self.loads[name] = load

    def add_vsource_element(self, name, bus, v):
        vsource_obj = Vsource(name, bus, v)
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
