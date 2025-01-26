from circuit import Circuit

class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow():
        
        # Check for circuit components
        if not self.circuit.vsource or not self.circuit.resistors or not self.circuit.loads:
            print("Circuit doesn't have necessary components\n")
        
        # Calculate total conductance
        total_conductance = 0
        for resistor in self.circuit.resistor.values():
            total_conductance += 1 / resistor.r

        # Calculate load conductance
        for load in self.circuit.load.values():
            total_conductance += 1 / load.v

        if total_conductance != 0:
            current = self.circuit.vsource.v * total_conductance
            self.circuit.set_i(current)
        else:
            print("Cannot calculate current")
    
        # Calculate voltage at bus B
        # V = I/R for series
        voltage_drop = self.circuit.i * list(self.circuit.resistors.values())[0].r
        bus_b_voltage = self.circuit.vsource.v - voltage_drop

        if 'B' in self.circuit.buses:
            self.circuit.buses['B'].v = bus_b_voltage

        self.circuit.print_nodal_voltage()
        self.circuit.print_circuit_current()
