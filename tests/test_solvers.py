#!/usr/bin/python3

import sys
import time
import unittest

import cube_data
import solvers

sys.path.append('../snake_cube')

class TestSolver(unittest.TestCase):

    def test_solutions_pass(self):
        """
        Solver should return all known rel solutions
        for each cube in cube_data
        """
        with open("test.log", "w") as fh: 
            CUBES = cube_data.CUBES 
            for cube in CUBES: 
                print("Cube of size ", cube["cube_side_length"]) 
                fh.write("Cube of size " + str(cube["cube_side_length"])) + "\n")
                for solver_dic in solvers.SOLVERS:
                    print("Solver:  ", solver_dic["name"]) 
                    fh.write("Solver:  " + str(solver_dic["name"]) + "\n")
                    solver = solver_dic["solver"] 
                    strip_lengths = cube["strip_lengths"] 
                    now = time.time() 
                    solver_sols = [tuple(sol) for sol in solver(strip_lengths)]
                    print("Time taken ", time.time() - now)
                    fh.write("Time taken " + str(time.time() - now) + "\n")
                    known_sols = [tuple(sol) for sol in cube["rel_solutions"]] 
                    for sol in solver_sols:
                        self.assertTrue(sol in known_sols)
                    for sol in known_sols:
                        self.assertTrue(sol in solver_sols)
                    print("Solutions correct")
                    fh.write("Solutions correct" + "\n")
        

if __name__ == '__main__':
    unittest.main()
