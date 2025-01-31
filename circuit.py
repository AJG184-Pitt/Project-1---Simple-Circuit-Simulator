from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource

class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.buses = dict()
        self.resistors = dict()
        self.loads = dict()
        self.vsources = dict()
        self.i = float

    def add_bus(self, name: str):
        bus_obj = Bus(name)
        self.buses[name] = bus_obj
         
    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        resistor_obj = Resistor(name, bus1, bus2, r)
        self.resistors[name] = resistor_obj

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        load_obj = Load(name, bus1, p, v)
        self.loads[name] = load_obj

    def add_vsource_element(self, name: str, bus1: str, v: float):
        vsource_obj = Vsource(name, bus1, v)
        self.vsources[name] = vsource_obj

    def set_i(self, current):
        self.i = float(current)

    # Prints out the circuit information including buses
    def print_nodal_voltage(self):
        print(f"Nodal voltage for circuit {self.name}")

        for bus_name, bus in self.buses.items():
            print(f"Bus: {bus_name}, Voltage: {bus.v:.3f}")

        # for vsource_name, vsource in self.vsources.items():
        #     print(f"Vsource name: {vsource.name}")
        #     print(f"Vsource bus: {vsource.bus1}")
        #     print(f"Vsource voltage: {vsource.v:.3f}")
        #
        # for load in self.loads.values():
        #     print(f"Load name: {load.name}")
        #     print(f"Load bus1: {load.bus1}")
        #     print(f"Load p: {load.p}")
        #     print(f"Load v: {load.v}")

    # Prints out the circuit current value
    def print_circuit_current(self):
        print(f"Current at circuit {self.name}")
        print(f"Circuit current: {self.i:.3f} A")
