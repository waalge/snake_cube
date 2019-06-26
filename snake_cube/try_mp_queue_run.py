"""
Trying to implement Toy that will play nicely with queues.
Seems slower than embarrasingly parallel.
"""

from multiprocessing import Process, Queue
import time, traceback, math
from mpToy import MPToy
import cube_data

def mp_toy_subprocess(strip_lengths, start, end, idle_queue, job_queue, solutions_queue):
    T = MPToy(strip_lengths, idle_queue, job_queue) 
    T.start(start) 
    T.run(finish_state = end) 
    print("I'm finished") 
    for rel_sol in  T.rel_solutions():
        solutions_queue.put(rel_sol) 
    
def str_vec(v):
    return "".join([str(xi) for xi in v])

if __name__ == "__main__":
    cube = cube_data.cubes[0]
    strip_lengths = cube["strip_lengths"] 

    job_queue = Queue()  
    idle_queue = Queue()  
    solutions_queue = Queue()  
    T = MPToy(strip_lengths, job_queue, idle_queue)
    starts, ends = T.split(split_into = 4)
    print("\n".join([str_vec(v) for v in starts])) 
    print("\n".join([str_vec(v) for v in ends])) 
    processes = []
    now = time.time() 
    for cnt in range(4): 
        p = Process(target=mp_toy_subprocess, args=(strip_lengths, starts[cnt], ends[cnt], idle_queue, job_queue, solutions_queue))
        p.start()
        processes.append(p) 
    results = [] 
    [p.join() for p in processes] 
    while not solutions_queue.empty():
        results.append(solutions_queue.get())
    print("Results")
    print("\n".join([str_vec(v) for v in sorted(results)])) 
    print(time.time() - now, sum([3 ** cnt for cnt in range(4)]), 3 **3 ) 

    

