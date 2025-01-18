from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource

class Circuit:
    def __init__(self, name, bus, resistor, load, vsource, current):
        self.name = name
        self.buses = dict()
        self.resistors = dict()
        self.loads = dict()
        self.vsource = vsource
        self.i = current

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
        self.vsource = v

    def set_i(self, current):
        self.i = current

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

        # Calculate the current based on values
        total_resistance = 0
        for resistor in self.resistors.values():
            total_resistance_calc += resistor.r
        
        total_resistance = total_resistance_calc
        
        # If statement for printing current
        if total_resistance != 0:
            current  = self.vsource / total_resistance
            print(f"Calculated current {current}")
        else:
            print("Cannot calculate current due to zero resistance")
