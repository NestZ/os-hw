from result import Result

class RoundRobin:
    def __init__(self, p_lst, q_time, cont_sw_time):
        self.p_lst = p_lst
        self.q_time = q_time
        self.cont_sw_time = cont_sw_time
    
    def run(self):
        num_process = len(self.p_lst)
        sum_time = 0
        exec_cnt = 0
        res_time = 0
        wait_time = 0
        turn_around_time = 0
        flag = True
        while flag == True:
            flag = False
            for p in self.p_lst:
                if p.run_time_left == 0:
                    continue
                flag = True
                exec_cnt += 1
                if p.run_time_left > self.q_time:
                    p.run_time_left -= self.q_time
                    sum_time += self.q_time
                else:
                    sum_time += p.run_time_left
                    turn_around_time += sum_time
                    p.run_time_left = 0
                if p.exec_cnt == 0:
                    p.res_time = sum_time
                p.exec_cnt += 1
                p.avg_wait_time = (sum_time - p.last_exec) / p.exec_cnt
                p.last_exec = sum_time
        sum_time += (exec_cnt - 1) * self.cont_sw_time
        for p in self.p_lst:
            wait_time += p.avg_wait_time
            res_time += p.res_time
        return Result(sum_time,
                wait_time / num_process,
                res_time / num_process,
                turn_around_time / num_process)
