# Load Class

# 3. Load
# a. Attributes:
# i. name (str): The user should provide this as an argument when defining
# the object.
# ii. bus1 (str): The user should provide this as an argument when defining the
# object.
# iii. p (float): The user should provide this as an argument when defining the
# object.
# iv. q (float): The user should provide this as an argument when defining the
# object.
# v. g (float): It should be calculated internally using the calc_g method.
# b. Methods:
# i. calc_g(): Calculates the conductance value

# note: instructions say to use q, but it likely represents the voltage ... changed to v

class Load:
    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v

        self.g = self.calc_g()

    def calc_g(self):
        return self.p/self.v**2 # assume v=1 pu at load ... P = V^2/R --> G = P/--> G = PV^2

