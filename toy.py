import numpy as np

def vector(vals):
    def vector(vals):
        return np.array(vals) 
    return np.array(vals) 

# Fix an ordering of orientations
ORIENTATIONS = [vector(vec) for vec in [
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (-1,0,0),
    (0,-1,0),
    (0,0,-1),
    ]] 

# Relative to absolute orientation wrt to ORIENTATIONS
CONVERSION = [
    [(0,1,0), (0,0,1), (0,-1,0), (0,0,-1)],
    [(0,0,1), (1,0,0), (0,0,-1), (-1,0,0)],
    [(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)],
    [(0,-1,0), (0,0,-1), (0,1,0), (0,0,1)],
    [(0,0,-1), (-1,0,0), (0,0,1), (1,0,0)],
    [(-1,0,0), (0,-1,0), (1,0,0), (0,1,0)],
    ]

class Toy(object):
    """
    """

    def __init__(self, list_of_lengths):
        """
        Toy of cublets attached by string that can be arranged into a cube.  
        """
        cube_size_3 = sum(list_of_lengths) - len(list_of_lengths) + 1
        self._cube_size = round((cube_size_3)**(1/3))
        assert self._cube_size**3 - cube_size_3 == 0, "not well defined input for cube" 
        self._strips = [Strip(k) for k in list_of_lengths] 
        #initial 
        self._strips[0].set_start(vector((0,0,0))) 
        self._strips[0].set_absolute_orientation(ORIENTATIONS[0]) 
        self._strips[1].set_relative_orientation(0)
        self._live_strip_n = 1 
        self.compute_next_coordinate()
        self._total_states = self._cube_size**(len(self._strips)-2)
        self._solutions = [] 
        self._fail_cnt = 0 
        pass 

    def compute_next_coordinate(self):
        live_n = self._live_strip_n
        live_strip = self._strips[live_n]
        old_strip = self._strips[live_n - 1]
        live_strip.set_start(old_strip.get_end()) 
        #print("x",self._live_strip_n, live_strip.get_start())
        live_strip.compute_orientaion(old_strip.get_absolute_orientation()) 

    def fail(self):
        """
        Fail conditions.
        Return 0 if nothing fails. 
        """
        self._fail_cnt += 1
        ## Outside of box. 
        cube_anchored = 1 
        for ii in (0,1,2):
            max_coordinate = max([p[ii] for p in self.ends()]+[0])  # start point
            min_coordinate = min([p[ii] for p in self.ends()]+[0]) 
            if max_coordinate - min_coordinate > 3: 
                # print("fail 1,", ii, max_coordinate, min_coordinate, self._strips[self._live_strip_n].get_end()) 
                #print([s.get_relative_orientation() for s in self._strips[:self._live_strip_n]])
                return 1
            elif max_coordinate - min_coordinate < 3:
                cube_anchored = 0 

        ## Overlap.
        coordinates_filled = [coord for strip in self._strips[:self._live_strip_n+1] for coord in strip.get_coordinates()[1:]]
        if len(list(set([tuple(x) for x in coordinates_filled]))) != len(coordinates_filled): 
            #print("fail 2,", [tuple(x) for x in coordinates_filled]) 
            return 2
        return 0

    def start(self, rel_orientations):
        """
        Fix initial rel orientations. 
        Can then run from some given state. 
        """
        for ii,ro in enumerate(rel_orientations):
            self._strips[ii].set_relative_orientation(ro)
            if ii > 0: 
                self._live_strip_n = ii 
                self.compute_next_coordinate() 
        #print(self.ends())

    def progress(self):
        """
        Crude progress bar
        """
        return sum([strip.get_relative_orientation() * self._cube_size**(len(self._strips) - ii - 1) for ii, strip in enumerate(self._strips) if 2<= ii <= self._live_strip_n])/ self._total_states

    def ends(self):
        """
        Ends of strips
        """
        return [tuple(s.get_end()) for s in self._strips[:self._live_strip_n+1]] 

    def rel_orientations(self):
        """
        Relative orietations of strips
        """
        return [s.get_relative_orientation() for s in self._strips[1:self._live_strip_n + 1]] 

    def finished(self): 
        """
        Termination condition
        """
        return self._strips[1].get_relative_orientation() != 0

    def run(self, verbose = False):
        """
        Iterate through all states until fail.
        Save solutions. 
        """
        previous_progress = 0
        while not self.finished():
            if self.fail():
                self.increment()
            elif self.solved():
                self._solutions.append(self.ends())
                if verbose: 
                    print("Solution found")
                    print(", ".join([str(tuple(x)) for x in self.ends()]))
                self.increment() 
            else:
                self.extend()
            if verbose:
                if self.progress() > previous_progress + 0.001:
                    print("Progress ", self.progress(), self._fail_cnt, self.rel_orientations())
                    previous_progress = self.progress() 

    def increment(self):
        """
        Increment rel orientations
        """
        while not self._strips[self._live_strip_n].increment_rel_orientation():
            self._live_strip_n += -1 
        self.compute_next_coordinate() 

    def extend(self):
        """
        Extend the live strip number
        """
        self._live_strip_n += 1 
        self._strips[self._live_strip_n].set_relative_orientation(0) 
        self.compute_next_coordinate()

    def solved(self): 
        """
        Solution found criteria (assumed hasn't failed)
        """
        return self._live_strip_n == len(self._strips) -1

    def solutions(self):
        return self._solutions

class Strip(object): 
    """
    """
    def __init__(self, length): 
        self._length = length

    def get_length(self):
        return self._length

    def set_relative_orientation(self, val):
        """
        Values 0,1,2,3 
        """
        self._rel_orientation = val

    def increment_rel_orientation(self):
        """
        """
        self._rel_orientation = (self._rel_orientation + 1) % 4
        return self._rel_orientation != 0

    def get_relative_orientation(self):
        return self._rel_orientation

    def get_coordinates(self):
        return [self._start + k * self._abs_orientation for k in range(self._length)]

    def set_start(self, coordinate):
        self._start = coordinate

    def get_start(self):
        return self._start

    def get_end(self):
        return self.get_coordinates()[-1]

    def set_coordinate(self, val):
        """
        """
        self._coordinate = val

    def get_coordinate(self):
        return self._coordinate

    def set_absolute_orientation(self, val):
        """
        """
        self._abs_orientation = vector(val)

    def get_absolute_orientation(self):
        return self._abs_orientation

    def compute_orientaion(self, prior_orientation):
        val = self._rel_orientation 
        prior_index = [(prior_orientation == v).all() for v in ORIENTATIONS].index(1)
        self._abs_orientation = vector(CONVERSION[prior_index][val] )


