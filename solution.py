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
        
        # Calculate total conductance
        total_conductance = 0
        for resistor in self.circuit.resistors.values():
            total_conductance += 1 / resistor.r

        # Calculate load conductance
        for load in self.circuit.loads.values():
            total_conductance += load.g

        if total_conductance != 0:
            current = vsource.v * total_conductance
            self.circuit.set_i(current)
        else:
            print("Cannot calculate current")
            return

        # Set voltage at source bus A
        if vsource.bus1 in self.circuit.buses:
            self.circuit.buses[vsource.bus1].v = vsource.v
    
        # Calculate voltage at bus B
        # V = I/R for series
        voltage_drop = self.circuit.i * list(self.circuit.resistors.values())[0].r
        bus_b_voltage = vsource.v - voltage_drop

        if 'B' in self.circuit.buses:
            self.circuit.buses['B'].v = bus_b_voltage

        self.circuit.print_nodal_voltage()
        self.circuit.print_circuit_current()
