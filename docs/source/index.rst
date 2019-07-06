.. snake_cube documentation master file, created by
   sphinx-quickstart on Tue Jun 18 15:12:11 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to snake_cube's documentation!
======================================

Find solutions to a snake_cube_
using python. 

.. _Python: http://www.python.org/
.. _snake_cube: https://en.wikipedia.org/wiki/Snake_cube

Contents:

.. toctree::
   :maxdepth: 2

   toy.rst
   mp_toy.rst
   visualize.rst
   solvers.rst

The main class is Toy which models the snake cube toy. 
This is handled by various solvers, 
some demonstrating some parallelization to finding a solution. 

We can also visualize solutions using ``vtk``. 
This makes it easier to use an output solution to actually solve the toy. 


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

