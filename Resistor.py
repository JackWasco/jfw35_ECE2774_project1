# Resistor Class

# 2. Resistor
# a. Attributes:
# i. name (str): The user should provide this as an argument when defining
# the object.
# ii. bus1 (str): The user should provide this as an argument when defining the
# object.
# iii. bus2 (str): The user should provide this as an argument when defining the
# object.
# iv. r (float): The user should provide this as an argument when defining the
# object.
# v. g (float): It should be calculated internally using the calc_g method.
# b. Methods:
# i. calc_g(): Calculates the conductance value.

class Resistor:
    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r

        self.g = self.calc_g()

    def calc_g(self):
        if self.r == 0: # error check for div by 0
            print("Resistance cannot be 0")
            return -1
        return 1/self.r

