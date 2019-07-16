"""
A selection of different solvers to compare methods.
Demonstates that embarrassinly parallel can be improved upon using `multiprocessing.Queue`.
"""
import asyncio
from multiprocessing import Pool, Process, Queue

from mp_toy import MPToy
from toy import Toy


def series_solver(strip_lengths):
    """
    The basic solver.
    Just run a depth first search, no tricks.
    """
    toy = Toy(strip_lengths)
    toy.run()
    return toy.rel_solutions()


def subprocess(strip_lengths, start, end):
    """
    Subprocess for embarrassinly parallel
    """
    toy = Toy(strip_lengths)
    toy.start(start)
    toy.run(finish_state=end)
    # print(start, toy.rel_solutions())
    return toy.rel_solutions()


def embarrassingly_parallel(strip_lengths):
    """
    Split the task into four at first branching point.
    Uses multiprocessing pool.
    """
    starts = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]]
    ends = starts[1:] + [None]
    args = list(zip([strip_lengths] * 4, starts, ends))
    # print(list(args))
    with Pool(processes=4) as pool:
        results = pool.starmap(subprocess, args)
    flat_results = [res for proc in results for res in proc]
    return flat_results


def embarrassingly_parallel_2(strip_lengths):
    """
    Split the task into 16 tasks at first, and second branching points.
    Uses multiprocessing pool.
    """
    starts = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 2],
        [0, 0, 0, 3],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 2],
        [0, 0, 1, 3],
        [0, 0, 2, 0],
        [0, 0, 2, 1],
        [0, 0, 2, 2],
        [0, 0, 2, 3],
        [0, 0, 3, 0],
        [0, 0, 3, 1],
        [0, 0, 3, 2],
        [0, 0, 3, 3],
    ]
    ends = starts[1:] + [None]
    args = list(zip([strip_lengths] * len(starts), starts, ends))
    # print(list(args))
    with Pool(processes=4) as pool:
        results = pool.starmap(subprocess, args)
    flat_results = [res for proc in results for res in proc]
    return flat_results


async def asyncio_subprocess(strip_lengths, start, end):
    """
    Subprocess for concurrent_asyncio
    """
    toy = Toy(strip_lengths)
    toy.start(start)
    toy.run(finish_state=end)
    # print(start, toy.rel_solutions())
    return toy.rel_solutions()


def concurrent_asyncio(strip_lengths):
    """
    Split the task into four at first branching point.
    Uses asycio.
    """
    starts = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]]
    ends = starts[1:] + [None]
    # args = list(zip([strip_lengths] * 4, starts, ends))
    loop = asyncio.get_event_loop()
    tasks = []
    for start, end in zip(starts, ends):
        tasks.append(
            asyncio.ensure_future(asyncio_subprocess(strip_lengths, start, end))
        )
    loop.run_until_complete(asyncio.gather(*tasks))
    flat_results = [res for task in tasks for res in task.result()]
    return flat_results


def mp_toy_subprocess(
    strip_lengths, start, end, idle_queue, job_queue, solutions_queue
):
    """
    Subprocess for mp_with_queues
    """
    toy = MPToy(strip_lengths, idle_queue, job_queue)
    toy.start(start)
    toy.run(finish_state=end)
    print("I'm finished")
    for rel_sol in toy.rel_solutions():
        solutions_queue.put(rel_sol)


def str_vec(vec):
    """
    Condense vecs used to print for convenient debugging.
    """
    return "".join([str(xi) for xi in vec])


def mp_with_queues(strip_lengths):
    """
    More intelligent parallel approach.
    """
    job_queue = Queue()
    idle_queue = Queue()
    solutions_queue = Queue()
    toy = MPToy(strip_lengths, job_queue, idle_queue)
    starts, ends = toy.split(split_into=4)
    # print("\n".join([str_vec(v) for v in starts]))
    # print("\n".join([str_vec(v) for v in ends]))
    processes = []
    for cnt in range(4):
        proc = Process(
            target=mp_toy_subprocess,
            args=(
                strip_lengths,
                starts[cnt],
                ends[cnt],
                idle_queue,
                job_queue,
                solutions_queue,
            ),
        )
        proc.start()
        processes.append(proc)
    results = []
    [proc.join() for proc in processes]
    while not solutions_queue.empty():
        results.append(solutions_queue.get())
    return results


SOLVERS = [
    {"name": "mp_with_queues solver", "solver": mp_with_queues},
    {"name": "embarrassingly_parallel solver", "solver": embarrassingly_parallel},
    {"name": "embarrassingly_parallel_2 solver", "solver": embarrassingly_parallel_2},
    {"name": "simple series solver", "solver": series_solver},
]


if __name__ == "__main__":
    embarrassingly_parallel([2, 2, 2, 2, 2, 2, 2])
