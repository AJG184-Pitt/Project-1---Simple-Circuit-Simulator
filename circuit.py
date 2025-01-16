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
        self.bus = Bus(name, v)
        self.buses['bus_name'] = name
        self.buses['bus_value'] = v

    def add_resistor_element(self, name, bus1, bus2, r, g):
        self.resistor = Resistor(name, bus1, bus2, r, g)
        self.resistors['resistor_name'] = name
        self.resistors['resistor_value'] = r

    def add_load_element(self, name, bus, p, q, g):
        self.load = Load(name, bus, p, q, g)
        self.loads['load_name'] = name
        self.loads['load_value'] = g

    def add_vsource_element(self, name, bus, v):
        self.vsource_obj = Vsource(name, bus, v)
        self.vsource = v

    def set_i(self, current):
        self.i = current

    def print_nodal_voltage(self):
        print(f"Nodal voltage for circuit {self.name}")

        if hasattr(self, 'bus'):
            print(f"Bus: {self.buses['bus_name']}")
            print(f"Bus voltage: {self.buses['bus_value']}")

        if hasattr(self, 'vsource'):
            print(f"Vsource name: {self.vsource.name}")
            print(f"Vsource bus: {self.vsource.bus1}")
            print(f"Vsource voltage: {self.vsource.v}")

    def print_circuit_current(self):
        print(f"Current at circuit {self.name}")

        if hasattr(self, 'i'):
            t
