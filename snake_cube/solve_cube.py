#!/usr/bin/python3

from toy import * 
import time

def cube4():
    strip_lengths = [ 3,4, 4,4, 2,4, 2,4, 2,2, 2,2, 2,2, 2,2, 2,3, 2,4, 3,3, 2,4, 2,3, 2,2, 2,2, 2,3, 2,2, 2,2, 4,2, 4 ]
    start = []
    start = [0, 0, 0, 3, 0, 0, 1, 2, 0, 3, 3, 0, 0, 2, 0, 2, 3, 3, 2, 1, 2, 2, 1, 3, 0, 0, 2, 1, 1, 3, 2, 1, 2, 3, 0, 0, 2]
    #start = [0, 0, 3, 0, 0, 2, 3, 0, 2, 0, 0, 1, 1, 1, 2, 0, 3, 3, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 3, 1, 2, 1, 0, 3, 3, 3, 3, 0] 
    #start = [0, 0, 3, 0, 0, 2, 3, 0, 1]
    return strip_lengths, start

def cube3():
    strip_lengths = [2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 
                     2, 2, 2, 3, 3, 2, 2, 2, 2,]
    start = [0,0]
    return strip_lengths, start

def cube2():
    strip_lengths = ([2, 2, 2, 2, 2, 2, 2, ])
    start = [0,0]
    return strip_lengths, start

if __name__ == "__main__": 
    strip_lengths, start = cube2() 
    rel_sols = []
    for start_ii in range(4):
        start_time = time.time() 
        start = [0,0,start_ii] 
        T = Toy(strip_lengths) 
        T.start(start)
        print("Begin from", start) 
        end = None 
        if start_ii < 3:
            end = [0,0,start_ii + 1] 
        T.run(finish_state = end)
        rel_sols.extend(T.rel_solutions()) 
        print("Time", time.time() - start_time) 
    with open("rel_solutions.py", "w") as fh:
        fh.write(str(rel_sols))
    #print(T.rel_solutions())
