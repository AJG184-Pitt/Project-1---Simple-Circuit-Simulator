import math
from circuit import Circuit

class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):
        # Check for circuit components
        if not self.circuit.vsources:
            print("Circuit missing voltage source")
            return
        if not self.circuit.resistors:
            print("Circuit missing resistors")
            return
        if not self.circuit.loads:
            print("Circuit missing loads")
            return

        vsource = next(iter(self.circuit.vsources.values()))
        resistor = list(self.circuit.resistors.values())[0]
        load = list(self.circuit.loads.values())[0]

        # Total resistance is series combination
        total_resistance = self.circuit.resistors["Rab"].r + self.circuit.loads["Lb"].r

        # Calculate current (I = V/R)
        circuit_current = self.circuit.vsources["VA"].v / total_resistance
        self.circuit.set_i(circuit_current)

        # Set voltage at source bus A
        if vsource.bus1 in self.circuit.buses:
            self.circuit.buses[vsource.bus1].v = self.circuit.vsources["VA"].v

        # Calculate voltage at bus B
        voltage_drop = self.circuit.i * self.circuit.resistors["Rab"].r
        bus_b_voltage = self.circuit.vsources["VA"].v - voltage_drop

        if 'B' in self.circuit.buses:
            self.circuit.buses['B'].v = bus_b_voltage

        self.circuit.print_nodal_voltage()
        self.circuit.print_circuit_current()
