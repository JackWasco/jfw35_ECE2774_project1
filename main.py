# main file for project 1, milestone 2-5

from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource
from Circuit import Circuit
from Solution import Solution

def main():
    circuit = Circuit("Simple DC Circuit") # create Circuit object

    circuit.add_bus("A") # create bus A
    circuit.add_bus("B") # create bus B

    circuit.add_vsource_element("Va","A",100.0) # create voltage source element
    circuit.add_resistor_element("Rab","A","B",5) # create resistor element
    circuit.add_load_element("Lb","A",2000.0,100.0) # create load element

    solution = Solution(circuit) # create solution object
    solution.do_power_flow() # run power flow calc

    circuit.print_nodal_voltage() # print voltages
    circuit.print_circuit_current() # print current

if __name__ == "__main__":
    main()



