from circuit import Circuit
from solution import Solution

# Circuit objects
circuit = Circuit("Wire_Test")
circuit.add_bus("Source")
circuit.add_bus("Load")
circuit.add_vsource_element("V1", "Source", 120.0)
circuit.add_resistor_element("Wire", "Source", "Load", 0.5)
circuit.add_load_element("Load1", "Load", 1500.0, 100.0)

# Solution object
solution = Solution(circuit)
solution.do_power_flow()
