class Process:
    def __init__(self, run_time):
        self.run_time = run_time
        self.run_time_left = run_time
        self.last_exec = 0
        self.res_time = -1
        self.avg_wait_time = 0
        self.exec_cnt = 0

    def __lt__(self, other):
        return self.run_time < other.run_time
        