#!/usr/bin/python3

import unittest
import os, sys
sys.path.append('../snake_cube')
import toy 
import solutions 


class TestSnakeCube(unittest.TestCase):

    def test_solutions_pass(self):
        """
        """
        T = toy.Toy([2,2]) 
        #self.assertEqual('foo'.upper(), 'FOO')
        pass

    def test_some_nonsolutions_fail(self):
        #self.assertTrue('FOO'.isupper())
        #self.assertFalse('Foo'.isupper())
        pass

    def test_small_cube_solved(self):
        s = 'hello world'
        #self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        #with self.assertRaises(TypeError):
            #s.split(2)
        pass

    

if __name__ == '__main__':
    unittest.main()

