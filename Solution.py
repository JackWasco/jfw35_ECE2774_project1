# a. Attributes:
# i. circuit (Circuit): When creating a solution object, you must pass a Circuit
# object as an argument.
# b. Methods:
# i. do_power_flow(): Solves the circuit by finding bus voltages and circuit
# current. First calculate the current using element conductance values,
# then determine the voltage at bus B. This algorithm is designed
# specifically for this circuit, as the main goal is to understand the coding
# implementation

from Circuit import Circuit

class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        resistor = list(self.circuit.resistors.values())[0] # get first resistor element
        load = list(self.circuit.loads.values())[0] # get first load element

        v_a = self.circuit.vsource.v  # get known voltage from voltage source
        self.circuit.buses["A"].set_bus_v(v_a) # set voltage at bus A

        resistor_r = 1/resistor.g # calculate resistance for resistor from g (per instructions)
        load_r = 1/load.g # calculate resistance for load from g (per instructions)

        i_tot = v_a/(resistor_r + load_r) # calculate current
        self.circuit.set_i(i_tot) # update current in circuit class

        v_b = v_a - i_tot * resistor_r # calculate voltage at bus B
        self.circuit.buses["B"].set_bus_v(v_b) # set voltage at bus B





