Solvers 
=======

.. automodule:: solvers

.. autofunction:: solvers.series_solver
.. autofunction:: solvers.embarrassingly_parallel
.. autofunction:: solvers.embarrassingly_parallel_2
.. autofunction:: solvers.mp_with_queues

Below is the output of the ``test_solvers`` test function. 
All solvers found correct solutions to some known cubes, 
found in ``cube_data.CUBES``. 
``mp_with_queues`` is notably faster on the large cube.

::

    Cube of size 2
    Solver:  mp_with_queues solver
    Time taken 0.10181832313537598
    Solutions correct
    Solver:  embarrassingly_parallel solver
    Time taken 0.12799787521362305
    Solutions correct
    Solver:  embarrassingly_parallel_2 solver
    Time taken 0.1070094108581543
    Solutions correct
    Solver:  simple series solver
    Time taken 0.04367828369140625
    Solutions correct
    Cube of size 3
    Solver:  mp_with_queues solver
    Time taken 70.74648237228394
    Solutions correct
    Solver:  embarrassingly_parallel solver
    Time taken 69.29563045501709
    Solutions correct
    Solver:  embarrassingly_parallel_2 solver
    Time taken 82.18489837646484
    Solutions correct
    Solver:  simple series solver
    Time taken 188.59162759780884
    Solutions correct
    Cube of size 4
    Solver:  mp_with_queues solver
    Time taken 3528.277454137802
    Solutions correct
    Solver:  embarrassingly_parallel solver
    Time taken 5591.474845170975
    Solutions correct
    Solver:  embarrassingly_parallel_2 solver
    Time taken 4452.935115814209
    Solutions correct
    Solver:  simple series solver
    Time taken 10254.960399866104
    Solutions correct


