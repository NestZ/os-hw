from result import Result

class FirstComeFirstServe:
    def __init__(self, p_lst):
        self.p_lst = p_lst
    
    def run(self):
        num_process = len(self.p_lst)
        sum_time = 0
        wait_time = 0
        res_time = 0
        turn_around_time = 0
        for p in self.p_lst:
            turn_around_time += sum_time + p.run_time
            sum_time += p.run_time
            wait_time += sum_time
            res_time += sum_time
        return Result(sum_time,
                wait_time / num_process, res_time / num_process,
                turn_around_time / num_process)
