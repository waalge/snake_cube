#!/usr/bin/python3

import unittest
import os, sys
sys.path.append('../snake_cube')
import toy 
import solutions 

class TestSnakeCube(unittest.TestCase):

    def test_solutions_pass(self):
        """
        Check that known solutions work
        """
        strip_lengths=[3, 4, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,
                       2, 4, 3, 3, 2, 4, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 4, 2, 4]
        known_rel_orientation_solutions = [
                ]
        T = toy.Toy(strip_lengths) 
        for start in known_rel_orientation_solutions:
            T.start(start)
            self.assertEqual(T.fail(), 0) # Doesn't fail
            self.assertEqual(T.solve(), 1) # Strips used. 
        pass

    def test_input(self): 
        """
        Check raises error if strips do not have the correct number of cubelets
        Some bad inputs.
        """
        strip_lengths=[3, 4, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,
                       2, 4, 3, 3, 2, 4, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 4]
        with self.assertRaises(ValueError):
            T = toy.Toy(strip_lengths) 

        strip_lengths=[1]
        with self.assertRaises(ValueError):
            T = toy.Toy(strip_lengths) 


    def test_some_nonsolutions_fail(self):
        #self.assertTrue('FOO'.isupper())
        #self.assertFalse('Foo'.isupper())
        pass

    def test_2_cube(self):
        """
        There is essentially only one 2-cube. 
        There are 444 solutions. 
        """
        strip_lengths = [2,2,2,2,2,2,2]
        T = toy.Toy(strip_lengths)
        T.run() 
        self.assertEqual(len(T.solutions()), 444) 

    

if __name__ == '__main__':
    unittest.main()

