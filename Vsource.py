# Vsource class

# a. Attributes:
# i. name (str): The user should provide this as an argument when defining
# the object.
# ii. bus1 (str): The user should provide this as an argument when defining the
# object.
# iii. v (float): The user should provide this as an argument when defining the
# object

class Vsource:
    def __init__(self, name: str, bus1: str, v: float):
        self.name = name
        self.bus1 = bus1
        self.v = v

