#!/usr/bin/python3

import os
import sys
import unittest

import solutions
import toy

sys.path.append('../snake_cube')

class TestSnakeCube(unittest.TestCase):

    def test_solutions_pass(self):
        """
        Check that known solutions work
        """
        strip_lengths=[3, 4, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,
                       2, 4, 3, 3, 2, 4, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 4, 2, 4]
        known_rel_orientation_solutions = [
        [0, 0, 3, 0, 0, 2, 3, 0, 2, 0, 0, 1, 1, 1, 2, 0, 3, 3, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 3, 1, 2, 1, 0, 3, 3, 3, 3, 0],
        [0, 0, 3, 0, 0, 2, 3, 0, 2, 0, 0, 1, 1, 1, 2, 0, 3, 3, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 3, 2, 1, 2, 3, 0, 2, 0, 0, 3],
        [0, 0, 3, 0, 0, 3, 2, 1, 3, 1, 1, 0, 0, 0, 3, 1, 2, 2, 3, 0, 3, 1, 0, 0, 3, 0, 0, 3, 3, 2, 0, 3, 0, 1, 2, 2, 2, 2, 1],
        [0, 0, 3, 0, 0, 3, 2, 1, 3, 1, 1, 0, 0, 0, 3, 1, 2, 2, 3, 0, 3, 1, 0, 0, 3, 0, 0, 3, 3, 2, 3, 0, 3, 2, 1, 3, 1, 1, 2],
        [0, 0, 3, 0, 2, 0, 1, 2, 2, 2, 2, 3, 3, 1, 2, 2, 1, 3, 2, 1, 2, 2, 3, 1, 2, 1, 3, 0, 2, 3, 2, 1, 2, 3, 0, 0, 2, 0, 3],
        [0, 0, 3, 0, 2, 0, 1, 2, 2, 2, 2, 3, 3, 1, 2, 2, 1, 3, 2, 1, 2, 2, 3, 1, 2, 1, 3, 0, 2, 3, 3, 0, 3, 2, 1, 1, 3, 1, 2],
        [0, 0, 3, 0, 2, 1, 0, 3, 3, 3, 3, 2, 2, 0, 3, 3, 0, 2, 3, 0, 3, 3, 2, 0, 3, 0, 2, 1, 3, 2, 2, 1, 2, 3, 0, 0, 2, 0, 3],
        [0, 0, 3, 0, 2, 1, 0, 3, 3, 3, 3, 2, 2, 0, 3, 3, 0, 2, 3, 0, 3, 3, 2, 0, 3, 0, 2, 1, 3, 2, 3, 0, 3, 2, 1, 1, 3, 1, 2],
                ]
        T = toy.Toy(strip_lengths)
        for start in known_rel_orientation_solutions:
            T.start(start)
            self.assertEqual(T.fail(), 0) # Doesn't fail
            self.assertEqual(T.solved(), 1) # Strips used.
        pass

    def test_some_nonsolutions_fail(self):
        """
        Check that known nonsolutions do NOT work
        """
        strip_lengths=[3, 4, 4, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,
                       2, 4, 3, 3, 2, 4, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 4, 2, 4]
        known_rel_orientation_solutions = [
        [0, 0, 3, 1, 2, 1, 0, 3, 3, 3, 3, 2, 2, 0, 3, 3, 0, 2, 3, 0, 3, 3, 2, 0, 3, 0, 2, 1, 3, 2, 3, 0, 3, 2, 1, 1, 3, 1, 2],
                ]
        T = toy.Toy(strip_lengths)
        for start in known_rel_orientation_solutions:
            T.start(start)
            self.assertEqual(T.fail(), 1) # DOES fail
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

    def test_2_cube(self):
        """
        There is essentially only one 2-cube.
        There are 6 solutions which you can draw by hand.
        """
        strip_lengths = [2,2,2,2,2,2,2]
        T = toy.Toy(strip_lengths)
        T.run()
        self.assertEqual(len(T.solutions()), 6)



if __name__ == '__main__':
    unittest.main()
