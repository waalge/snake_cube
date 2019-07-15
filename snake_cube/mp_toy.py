"""
Similar to toy but handles queues within the run routine.
And has some addtional helpful functions.
"""

import math

import toy

vec = toy.vec
ORIENTATIONS = toy.ORIENTATIONS
CONVERSION = toy.CONVERSION


def str_vec(a_vec):
    """
    Condense vecs used to print for convenient debugging.
    """
    return "".join([str(xi) for xi in a_vec])


class MPToy(toy.Toy):
    """
    Toy with run method altered to handle queues.
    """

    def __init__(self, strip_lengths, idle_queue, job_queue):
        super().__init__(strip_lengths)
        self._idle_queue = idle_queue
        self._job_queue = job_queue

    def split(self, finish_val=None, split_into=2):
        """
        Split the current finish_val into two
        """
        if finish_val is None:
            finish_val = self._total_states
        current_val = self.enumerate_state()
        mid_vals = [
            round(current_val + cnt * (finish_val - current_val) / split_into)
            for cnt in range(split_into)
        ]
        starts = [self.evaluate_state_val(val) for val in mid_vals]
        ends = starts[1:] + [self.evaluate_state_val(finish_val)]
        return starts, ends

    def evaluate_state_val(self, state_val):
        """
        Inverse to enumerate_state function.
        """
        n_states = len(self._strips)
        state_vector = [0] * n_states
        for cnt in range(n_states):
            state_vector[cnt] = math.floor(state_val / 4 ** (n_states - cnt - 1))
            state_val += -state_vector[cnt] * 4 ** (n_states - cnt - 1)
        return state_vector

    def run(self, finish_state=None, verbose=False):
        """
        Similar to Toy.run but puts and gets items on queues appropriately.
        """
        previous_progress = 0
        if finish_state is None:
            finish_val = self._total_states  # Should be max value of a run
        else:
            finish_val = self.enumerate_state(finish_state)

        loop_cnt = 0
        idle_queue_check_threshold = 5000
        while self.enumerate_state() < finish_val:
            loop_cnt += 1
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
                    print(
                        "Progress ",
                        self.progress(),
                        self._fail_cnt,
                        self.rel_orientations(),
                    )
                    previous_progress = self.progress()
            if loop_cnt > idle_queue_check_threshold:
                loop_cnt = 0
                if not self._idle_queue.empty():
                    # print("I'm splitting", finish_val)
                    self._idle_queue.get()
                    start_end = self.split(finish_val)
                    self._job_queue.put(start_end)
                    finish_val = self.enumerate_state(start_end[1][0])
                    # print("split", finish_val)
        try:
            if self._idle_queue.qsize() >= 3:
                # print("ALL IDLE")
                for cnt in range(4):
                    self._job_queue.put("QUIT")
                return None
            self._idle_queue.put("idle")
            # print("I'm idle", finish_val, self._idle_queue)
            start_end = self._job_queue.get()
            if start_end == "QUIT":
                return None
            start = start_end[0][1]
            end = start_end[1][1]
            # print("New job", str_vec(start), str_vec(end))

            self.start(start)
            self.run(end)
        except:
            pass
