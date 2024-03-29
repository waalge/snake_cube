snake_cube 
==========

Find all solutions to any [snake cube](https://en.wikipedia.org/wiki/Snake_cube) using python. 

Solve a new cube?
=================

`example.py` contains a simple example. 

Lets fix some vocab for talking about snake cubes.

A snake cube is a collection of _cubelets_ attached with a taut string.
We wish to arrange the cubelets into a cube, the side length of which is the _cube size_
There are two _end cubelets_ in which the string terminates. 
There are a number of _join cubelets_ in which the string does not enter/exit the cubelet via opposite faces. 
A _strip_ is a sequence of adjacent cubelets which begin and end with either join cubelets or a join cubelet and an end cubelet, 
and between which there are no other join cubelets. 
The _length_ of a strip is the number of cublets between its begining and end (inclusive!).
Note that the minimum length of a strip is 2. 
The snake cube consists of a sequence of strips each of which shares its end with the beginning of the next strip. 

1. Unwind the snake cube into a flat stair case type arrangement, 
so that starting from one end the strips alternate from going right and going up.
 
2. Get the `strip_lengths` of a snake cube. 
This is presented of a list of ints of the strip lengths starting from the bottom left hand corner.
Note that even indexed entries correspond to strips going right;
odd indexed entries correspond to strips going up. 

3. Check that the total sum of all the strip lengths, 
minus the number of strips is one less than the cube of the cube size. 

4. Make an instance of `toy = toy.Toy(strip_lengths)`.
Run `toy.run()` to find all solutions. 
This may take some time. 
You can run in verbose mode with updates on progress. 
If its big (cube size >3) try running it in parallel. See `solvers.mp_with_queue`

5. Dump `toy.solutions()` to a file.

6. Visualize an absolute solution using `visualize.py`. 
Use this to help solve the snake cube toy. 

## A Visual

A short screen recording of an example output of `visualize.py` is [here](https://youtu.be/DDIHet0Mnbo). 

