#!/usr/bin/python3

from toy import * 

if __name__ == "__main__": 
    strip_lengths = ([2,3,4,3,2,3,2,3,2,3,2,3,5])
    start = ([0,0,0,0,0,0,0,0,0,0,0,0])
    strip_lengths = [ 3,4, 4,4, 2,4, 2,4, 2,2, 2,2, 2,2, 2,2, 2,3, 2,4, 3,3, 2,4, 2,3, 2,2, 2,2, 2,3, 2,2, 2,2, 4,2, 4 ]
    start = []
    start = [0, 0, 0, 3, 0, 0, 1, 2, 0, 3, 3, 0, 0, 2, 0, 2, 3, 3, 2, 1, 2, 2, 1, 3, 0, 0, 2, 1, 1, 3, 2, 1, 2, 3, 0, 0, 2]
    #start = [0, 0, 3, 0, 0, 2, 3, 0, 2, 0, 0, 1, 1, 1, 2, 0, 3, 3, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 3, 1, 2, 1, 0, 3, 3, 3, 3, 0] 
    start = [0, 0, 3, 0, 0, 2, 3, 0, 1]

    T = Toy(strip_lengths) 
    if start: 
        T.start(start)
    print("Begin from", start) 
    local_min = len(T._strips) 
    T.run(verbose=True) 
    with open("rel_solutions.py", "w") as fh:
        fh.write(str(T.rel_solutions()))
