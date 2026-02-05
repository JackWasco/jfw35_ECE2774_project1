# Circuit Class

# a. Attributes:
# i. name (str): The user should provide this as an argument when defining
# the object.
# ii. buses (Dict[str, Bus]): A dictionary where each item has a bus name as
# the key and its corresponding Bus object as the value. The Bus object is
# created using the add_bus method of the Circuit class.
# iii. resistors (Dict[str, Resistor]): A dictionary where each item has a resistor
# name as the key and its corresponding Resistor object as the value. The
# Resistor object is created using the add_resistor method of the Circuit
# class.
# iv. loads (Dict[str, Load]): A dictionary where each item has a load name as
# the key and its corresponding Load object as the value. The Load object
# is created using the add_load method of the Circuit class.
# v. vsource (Vsource): A VSource object. The Vsource object is created
# using the add_vsource method of the Circuit class.
# vi. i (float): Current flowing through the circuit. It should be updated during
# the power flow calculation.

# b. Methods:
# i. add_bus(bus: str): Adds a bus to the circuit.
# ii. add_resistor_element(name: str, bus1: str, bus2: str, r: float): Adds a
# resistor to the circuit.
# iii. add_load_element(name: str, bus1: str, p: float, v: float): Adds a load to
# the circuit.
# iv. add_vsource_element(name: str, bus1: str, v: float): Adds a voltage
# source to the circuit.
# v. set_i(i: float): Updates the i attribute.
# vi. print_nodal_voltage(): Prints voltages at all buses.
# vii. print_circuit_current(): Prints circuit current

from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource


class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.buses = {}
        self.resistors = {}
        self.loads = {}

        self.vsource = None
        self.i = None

    def add_bus(self, bus: str):
        self.buses[bus] = Bus(bus)

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        self.resistors[name] = Resistor(name,bus1, bus2, r)

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        self.loads[name] = Load(name,bus1, p, v)

    def add_vsource_element(self, name: str, bus1: str, v: float):
        self.vsource = Vsource(name,bus1, v)

    def set_i(self, i: float):
        self.i = i

    def print_nodal_voltage(self):
        print("\nNodal Voltages:")
        for bus_name, bus in self.buses.items():
            if bus.v is not None:
                print(f"{bus_name}: {bus.v:.1f} V")
            else:
                print(f"{bus_name}: Not set")

    def print_circuit_current(self):
        print("\nCircuit Current:")
        print(f"{self.i:.1f} A")

