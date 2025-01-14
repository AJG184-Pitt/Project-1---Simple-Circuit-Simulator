import numpy as np
import pandas as pd

class bus:
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @classmethod
    def set_bus_v(self, voltage):
        self.v = voltage
