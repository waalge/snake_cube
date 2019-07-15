#!/usr/bin/python3

import os
import sys
import unittest

sys.path.append("../snake_cube")

import cube_data
import toy


class TestSnakeCube(unittest.TestCase):
    def test_solutions_pass(self):
        """
        Check that known solutions work
        """
        cube = cube_data.CUBES[2]
        strip_lengths = cube["strip_lengths"]
        rel_solutions = cube["rel_solutions"]
        T = toy.Toy(strip_lengths)
        for start in rel_solutions:
            T.start(start)
            self.assertEqual(T.fail(), 0)  # Doesn't fail
            self.assertEqual(T.solved(), 1)  # Strips used.
        pass

    def test_some_nonsolutions_fail(self):
        """
        Check that known nonsolutions do NOT work
        """
        cube = cube_data.CUBES[2]
        strip_lengths = cube["strip_lengths"]
        rel_solution = cube["rel_solutions"][0]
        rel_solution[-1] = (rel_solution[-1] + 1)%3
        T = toy.Toy(strip_lengths)
        T.start(rel_solution)
        self.assertEqual(T.fail(), 1)  # DOES fail
        pass

    def test_input(self):
        """
        Check raises error if strips do not have the correct number of cubelets
        Some bad inputs.
        """
        cube = cube_data.CUBES[2]
        strip_lengths = cube["strip_lengths"][:-1]
        with self.assertRaises(ValueError):
            T = toy.Toy(strip_lengths)

        strip_lengths = [1]
        with self.assertRaises(ValueError):
            T = toy.Toy(strip_lengths)

    def test_2_cube(self):
        """
        There is essentially only one 2-cube.
        There are 6 solutions which you can draw by hand.
        """
        strip_lengths = [2, 2, 2, 2, 2, 2, 2]
        T = toy.Toy(strip_lengths)
        T.run()
        self.assertEqual(len(T.solutions()), 6)


if __name__ == "__main__":
    unittest.main()
