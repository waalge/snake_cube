"""
A simple example: 
    - Solve a snake cube of length 3
    - write all solutions to `example_solutions.py`
    - visualize the first solution 
"""

import toy
import visualize 

if __name__ == "__main__": 
    strip_lengths = [2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2]
    toy = toy.Toy(strip_lengths) 
    toy.run()
    if toy.solutions():
        print("I found " + str(len(toy.solutions())) + " solutions! =D")
        file_name = "example_solutions.py" 
        with open(file_name, 'w') as fh:
            fh.write("strip_lengths = " + str(strip_lengths) + "\n\n")
            str_sols = "".join(["    " + str(sol)+",\n" for sol in toy.solutions()]) 
            fh.write("solutions = {\n" + str_sols + "    }")
        print("solutions written to `" + file_name + "`")
        # Visualizing a solution
        print("... visualizing ...")
        visualize.visualize(toy.solutions()[0]) 

    else: 
        print("I found no solutions :'(")

