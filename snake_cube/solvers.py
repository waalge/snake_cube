from toy import Toy

def series_solver(strip_lengths):
    """
    The basic solver.
    Just run a depth first search, no tricks. 
    """
    T = Toy(strip_lengths) 
    T.run()
    return T.rel_solutions() 


import multiprocessing

def subprocess(strip_lengths, start, end): 
    T = Toy(strip_lengths) 
    T.start(start)
    T.run(finish_state = end)
    #print(start, T.rel_solutions())
    return T.rel_solutions() 

def embarrassingly_parallel(strip_lengths):
    """
    Split the task into four at first branching point. 
    Uses multiprocessing pool.
    """
    starts = [[0,0,0], [0,0,1], [0,0,2], [0,0,3]]
    ends = starts[1:] + [None] 
    args = list(zip([strip_lengths] * 4, starts, ends) )
    #print(list(args)) 
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(subprocess, args)
    flat_results = [res for proc in results for res in proc] 
    return flat_results

def embarrassingly_parallel_2(strip_lengths):
    """
    Split the task into 16 tasks at first, and second branching points. 
    Uses multiprocessing pool.
    """
    starts = [
            [0,0,0,0], [0,0,0,1], [0,0,0,2], [0,0,0,3], 
            [0,0,1,0], [0,0,1,1], [0,0,1,2], [0,0,1,3], 
            [0,0,2,0], [0,0,2,1], [0,0,2,2], [0,0,2,3], 
            [0,0,3,0], [0,0,3,1], [0,0,3,2], [0,0,3,3], 
            ]
    ends = starts[1:] + [None] 
    args = list(zip([strip_lengths] * len(starts), starts, ends) )
    #print(list(args)) 
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(subprocess, args)
    flat_results = [res for proc in results for res in proc] 
    return flat_results

import asyncio

async def asyncio_subprocess(strip_lengths, start, end): 
    T = Toy(strip_lengths) 
    T.start(start)
    T.run(finish_state = end)
    #print(start, T.rel_solutions())
    return T.rel_solutions() 

def concurrent_asyncio(strip_lengths):
    """
    Split the task into four at first branching point. 
    Uses asycio.
    """
    starts = [[0,0,0], [0,0,1], [0,0,2], [0,0,3]]
    ends = starts[1:] + [None] 
    args = list(zip([strip_lengths] * 4, starts, ends) )
    loop = asyncio.get_event_loop()
    tasks = [] 
    for start, end in zip(starts, ends): 
        tasks.append(asyncio.ensure_future(asyncio_subprocess(strip_lengths, start, end)))
    loop.run_until_complete(asyncio.gather(*tasks))
    flat_results = [res for task in tasks for res in task.result()] 
    return flat_results
from multiprocessing import Process, Queue
from mpToy import MPToy

def mp_toy_subprocess(strip_lengths, start, end, idle_queue, job_queue, solutions_queue):
    T = MPToy(strip_lengths, idle_queue, job_queue) 
    T.start(start) 
    T.run(finish_state = end) 
    print("I'm finished") 
    for rel_sol in  T.rel_solutions():
        solutions_queue.put(rel_sol) 
    
def str_vec(v):
    return "".join([str(xi) for xi in v])

def mp_with_queues(strip_lengths):
    job_queue = Queue()  
    idle_queue = Queue()  
    solutions_queue = Queue()  
    T = MPToy(strip_lengths, job_queue, idle_queue)
    starts, ends = T.split(split_into = 4)
    #print("\n".join([str_vec(v) for v in starts])) 
    #print("\n".join([str_vec(v) for v in ends])) 
    processes = []
    for cnt in range(4): 
        p = Process(target=mp_toy_subprocess, args=(strip_lengths, starts[cnt], ends[cnt], idle_queue, job_queue, solutions_queue))
        p.start()
        processes.append(p) 
    results = [] 
    [p.join() for p in processes] 
    while not solutions_queue.empty():
        results.append(solutions_queue.get())
    return results

solvers = [
        {
            "name":"mp_with_queues solver", 
            "solver": mp_with_queues
        },
        {
            "name":"embarrassingly_parallel solver", 
            "solver": embarrassingly_parallel
        },
        {
            "name":"embarrassingly_parallel_2 solver", 
            "solver": embarrassingly_parallel_2
        },
        {
            "name":"simple series solver", 
            "solver": series_solver
        },
        ]


if __name__ == "__main__":
    embarrassingly_parallel([2,2,2,2,2,2,2]) 

