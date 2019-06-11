import numpy as np

def vector(vals):
    def vector(vals):
        return np.array(vals) 
    return np.array(vals) 

class Toy(object):
    """
    """

    def __init__(self, list_of_lengths):
        """
        """
        self._strip_lengths = list_of_lengths 
        self._strips = [Strip(k) for k in list_of_lengths] 
        self._joins = [Join() for k in list_of_lengths]
        self._live_join = 2

    def start(self):
        """
        """
        self._joins[0].set_orientation = 0
        self._joins[0].set_coordinate = vector((0,0,0))
        self._strips.set_orientation = vector((1,0,0)
        ... 

    def fail(self):
        ## Outside of box. 
        for ii in (0,1,2):
            max_coordinate = max([p.get_coordinate()[ii] for p in self._joins[:self._live_join]]) 
            min_coordinate = min([p.get_coordinate()[ii] for p in self._joins[:self._live_join]]) 
            if max_coordinate - min_coordinate > 3: 
                return 0

        ## Overlap.
        coordinates_filled = [strip.compute_coordinates(join.get_coordinate()) for strip, join in zip(self._strips, self._joins)[:self._live_join]]
        if len(list(set(coordinates_filled))) != len(coordinates_filled): 
            return 0

        return 1

    def increment_toy(self):
        if self.fail():
            if self._joins[self._live_join].get_orientation == 3:
                self._joins[self._live_join] = Join()
                self._live_join += -1 
            else:
                self._joins[self._live_join].set_orientation += 1
        else: 
            self._live_join += 1 
        if self._live_join > len(self._joins): 
            print("Yay") 

class Strip(object): 
    """
    """
    def __init__(self, length): 
        self._length = length

    def get_length(self):
        return self._length

    def set_orientation(self, val):
        """
        Values  permuations of (\pm 1,0,0)
        """
        self._orientation = val

    def get_orientation(self):
        return self._orientation

    def compute_coordinates(self, start):
        return [start + k * self._orientation for k in range(self._length)]

class Join(object): 
    """
    """
    def __init__(self): 
        self._orientation = 0

    def set_orientation(self, val):
        """
        Values 0, 1, 2, 3
        """
        self._orientation = val

    def get_orientation(self):
        return self._orientation

    def set_coordinate(self, val):
        """
        """
        self._coordinate = val

    def get_coordinate(self):
        return self._coordinate
