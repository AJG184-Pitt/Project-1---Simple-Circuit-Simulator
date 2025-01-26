import numpy as np
import pandas as pd
from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource
from circuit import Circuit
from solution import Solution

# Circuit objects
circuit = Circuit("Test")
circuit.add_bus("A")
circuit.add_bus("B")
circuit.add_vsource_element("VA", "A", 100.0)
circuit.add_resistor_element("Rab", "A", "B", 5)
circuit.add_load_element("Lb", "B", 2000.0, 100.0)

# Solution object
solution = Solution(circuit)
solution.do_power_flow()
