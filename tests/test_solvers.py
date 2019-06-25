#!/usr/bin/python3

import unittest
import os, sys
import time 

sys.path.append('../snake_cube')
import cube_data 
import solvers

class TestSolver(unittest.TestCase):

    def test_solutions_pass(self):
        """
        Solver should return all known rel solutions
        for each cube in cube_data 
        """
        cubes = cube_data.cubes 
        for cube in cubes: 
            print("Cube of size ", cube["cube_side_length"]) 
            for solver_dic in solvers.solvers:
                print("Solver ", solver_dic["name"]) 
                solver = solver_dic["solver"] 
                strip_lengths = cube["strip_lengths"] 
                now = time.time() 
                solver_sols = [tuple(sol) for sol in solver(strip_lengths)]
                print("Time taken ", time.time() - now)
                known_sols = [tuple(sol) for sol in cube["rel_solutions"]] 
                for sol in solver_sols:
                    self.assertTrue(sol in known_sols) 
                for sol in known_sols:
                    self.assertTrue(sol in solver_sols) 
                print("Solutions correct")
    

if __name__ == '__main__':
    unittest.main()

