"""
Model of snake cube: a toy made of strips of cubelets that can be rotated into a n-cube.
The run method finds all solutions from the given start.
"""
import numpy as np

def vec(vals):
    """
    Short hand for a vector (numpy array) 
    :param list vals: list of numeric values representing a vector
    :returns:   np array of vals
    :rtype:     np array
    """
    return np.array(vals)

# Fix an ordering of orientations
ORIENTATIONS = [vec(vals) for vals in [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
    ]]

# Relative to absolute orientation wrt to ORIENTATIONS
CONVERSION = [
    [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)],
    [(0, 0, 1), (1, 0, 0), (0, 0, -1), (-1, 0, 0)],
    [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)],
    [(0, -1, 0), (0, 0, -1), (0, 1, 0), (0, 0, 1)],
    [(0, 0, -1), (-1, 0, 0), (0, 0, 1), (1, 0, 0)],
    [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0)],
    ]

class Toy(object):
    """
    Toy of cublets attached by string that can be arranged into a cube.

    :param list strip_lengths: List of strip lengths
    :raises ValueError: If number of cubelets corresponding to `strip_length` is not a cube number.
    """

    def __init__(self, strip_lengths):
        cube_size_3 = sum(strip_lengths) - len(strip_lengths) + 1
        self._cube_size = round((cube_size_3)**(1/3))
        if self._cube_size**3 - cube_size_3 != 0:
            raise(ValueError, "Number of cubelets must equal a cube number")
        self._strips = [Strip(k) for k in strip_lengths]
        #initial
        self._strips[0].set_start(vec((0, 0, 0)))
        self._strips[0].set_abs_orientation(ORIENTATIONS[0])
        self._strips[1].set_rel_orientation(0)
        self._live_strip_n = 1
        self.compute_next_coordinate()
        self._total_states = self._cube_size**(len(self._strips)-2)
        self._solutions = []
        self._rel_solutions = []
        self._fail_cnt = 0
        pass

    def compute_next_coordinate(self):
        """
        Compute properties of live strip from previous strip and rel orientation.
        """
        live_n = self._live_strip_n
        live_strip = self._strips[live_n]
        old_strip = self._strips[live_n - 1]
        live_strip.set_start(old_strip.get_end())
        #print("x",self._live_strip_n, live_strip.get_start())
        live_strip.compute_orientaion(old_strip.get_abs_orientation())

    def fail(self):
        """
        A series of conditions that if any are met mean the current state cannot lead to a solution.

        :returns:   0 if no immediate reason why the current state cannot reach a solution.
                    Otherwise a positive int corresponding to the which condition failed.
        :rtype: int
        """
        self._fail_cnt += 1
        ## Outside of box.
        for ii in (0, 1, 2):
            max_coordinate = max([p[ii] for p in self.ends()]+[0])  # start point
            min_coordinate = min([p[ii] for p in self.ends()]+[0])
            if max_coordinate - min_coordinate > 3:
                return 1

        ## Overlap. This is not efficient. Should just check latest new strip.
        coordinates_filled = [coord for strip in self._strips[:self._live_strip_n+1]
                              for coord in strip.get_coordinates()[1:]] + [vec((0, 0, 0))]
        if len(list(set([tuple(x) for x in coordinates_filled]))) != len(coordinates_filled):
            #print("fail 2,", [tuple(x) for x in coordinates_filled])
            return 2
        return 0

    def start(self, rel_orientations):
        """
        Fix initial rel orientations.
        Can then run from some given state.

        :param list rel_orientations: list of length k of ints 0 - 3
                corresponding to the initial orientations of the initial k strips
        """
        for ii, rel_orientation in enumerate(rel_orientations):
            self._strips[ii].set_rel_orientation(rel_orientation)
            if ii > 0:
                self._live_strip_n = ii
                self.compute_next_coordinate()
        #print(self.ends())

    def progress(self):
        """
        A crude progress bar: A strictly monotonic map from the current state to the interval [0,1)

        """
        return sum([strip.get_relative_orientation() * self._cube_size
                    ** (len(self._strips) - ii - 1) for ii, strip in enumerate(self._strips)
                    if 2 <= ii <= self._live_strip_n]) / self._total_states

    def ends(self):
        """
        :returns:   Coordinates of the ends of strips up to and including the current live strip
        :rtype:     list
        """
        return [tuple(s.get_end()) for s in self._strips[:self._live_strip_n+1]]

    def rel_orientations(self):
        """
        :returns:   Relative orietations of strips up to and including the current live strip
        :rtype:     list
        """
        return [s.get_relative_orientation() for s in self._strips[1:self._live_strip_n + 1]]

    def finished(self):
        """
        :returns:   1 if finished ie incrementing first strip which we have fixed to 0, 0 otherwise
        :rtype:     int
        """
        return self._strips[1].get_relative_orientation() != 0

    def run(self, verbose=False):
        """
        Iterate through all states until fail.
        Record solutions when found.

        :param bool verbose:   Print regular progress if True
        """
        previous_progress = 0
        while not self.finished():
            if self.fail():
                self.increment()
            elif self.solved():
                self._solutions.append(self.ends())
                self._rel_solutions.append(self.rel_orientations())
                if verbose:
                    print("Solution found")
                    print(", ".join([str(x) for x in self.rel_orientations()]))
                self.increment()
            else:
                self.extend()
            if verbose:
                if self.progress() > previous_progress + 0.01:
                    print("Progress ", self.progress(), self._fail_cnt, self.rel_orientations())
                    previous_progress = self.progress()

    def increment(self):
        """
        Increment rel orientations, and update live strip number appropriately, assuming failed.
        """
        while not self._strips[self._live_strip_n].increment_rel_orientation():
            self._live_strip_n += -1
        self.compute_next_coordinate()

    def extend(self):
        """
        Increment rel orientations, and update live strip number appropriately, assuming NOT failed.
        """
        self._live_strip_n += 1
        self._strips[self._live_strip_n].set_rel_orientation(0)
        self.compute_next_coordinate()

    def solved(self):
        """
        :returns:   1 if solved ie live strip is ultimate, and ASSUMED NOT failed, 0 otherwise
        :rtype:     int
        """
        return self._live_strip_n == len(self._strips) -1

    def solutions(self):
        """
        :returns:   All solutions as ends found in run.
        :rtype:     list
        """
        return self._solutions

    def rel_solutions(self):
        """
        :returns:   All solutions as rel orientations found in run.
        :rtype:     list
        """
        return self._rel_solutions

class Strip(object):
    """
    Strip of cubelets that make up a single component of toy.

    :param int length: number of cubelets in strip.
    :raises ValueError: If length is not at least 2
    """
    def __init__(self, length):
        if length < 2:
            raise(ValueError, "Length of strip must be at least 2")
        self._length = length
        self._rel_orientation = None
        self._abs_orientation = None
        self._start = None

    def get_length(self):
        """
        :returns:   length
        :rtype:     int
        """
        return self._length

    def set_rel_orientation(self, val):
        """
        Set the relative orientation

        :param int val: 0 - 3 corresponding to the convertion convention established
                        in the constants ORIENTATIONS, CONVERSION.
        """
        self._rel_orientation = val

    def increment_rel_orientation(self):
        """
        Increment the relative orientation

        :returns:   1 if increment has gone from 3 to 0, and 0 otherwise
        :rtype:     int
        """
        self._rel_orientation = (self._rel_orientation + 1) % 4
        return self._rel_orientation != 0

    def get_relative_orientation(self):
        """
        Increment the relative orientation

        :returns:  0 - 3 corresponding to the convertion convention established
                        in the constants ORIENTATIONS, CONVERSION.
        :rtype:     int
        """
        return self._rel_orientation

    def get_coordinates(self):
        """
        :returns:   list of coordinates from start to end
        :rtype:     list
        """
        return [self._start + k * self._abs_orientation for k in range(self._length)]

    def set_start(self, coordinate):
        """
        Set the start coordinate

        :param vec coordinate: vec or tuple of coordinates of start of strip
        """
        self._start = vec(coordinate)

    def get_start(self):
        """
        :returns:   start coordinate of vec
        :rtype:     vec
        """
        return self._start

    def get_end(self):
        """
        :returns:   end coordinate of vec
        :rtype:     vec
        """
        return self.get_coordinates()[-1]

    def set_abs_orientation(self, val):
        """
        Manually fix absolute orientation.
        Used on initial strips.

        :param vec val: vec or tuple of abs orientation
        """
        self._abs_orientation = vec(val)

    def get_abs_orientation(self):
        """
        :returns:   absolute orientation
        :rtype:     vec
        """
        return self._abs_orientation

    def compute_orientaion(self, prior_orientation):
        """
        compute abs orientation from orientation of previous strip abs orientation
        and own rel orientation using conventions.

        :param vec prior_orientation: vec of abs orientation of previous strip
        """
        val = self._rel_orientation
        prior_index = [(prior_orientation == v).all() for v in ORIENTATIONS].index(1)
        self._abs_orientation = vec(CONVERSION[prior_index][val])


