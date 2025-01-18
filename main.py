import numpy as np
import pandas as pd
from bus import Bus
from load import Load
from resistor import Resistor
from vsource import Vsource

print("Output versions")
print("===============")
print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("\n")

# Test load class
load = Load("load", "bus", 2, 2, 3)

print("Load class values")
print("=================")
print(load.name)
print(load.bus1)
print(load.p)
print(load.q)
print(load.g)

# Test bus class
bus = Bus("Bus1", 5)
print(bus.name)
print(bus.v)
