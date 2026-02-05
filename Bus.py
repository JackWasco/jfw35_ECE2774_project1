# Bus Class

# Bus
# a. Attributes:
# i. name (str): The user should provide this as an argument when defining
# the object.
# ii. v (float): Represents the voltage at the bus. For buses connected to a
# voltage source, the voltage updates when the source is created. For all
# other buses, the voltage updates during the power flow calculation.
# b. Methods:
# i. set_bus_v(bus_v: float): Sets the voltage at the bus

class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v = None  # voltage is set later by source or power flow calc

    def set_bus_v(self, bus_v: float):
        self.v = bus_v