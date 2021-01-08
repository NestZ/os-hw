import random
from fcfs import FirstComeFirstServe
from sjf import ShortestJobFirst
from rr import RoundRobin
from process import Process

PROCESS_CNT = 60
BOUND_1 = (2, 8)
BOUND_2 = (20, 30)
BOUND_3 = (35, 40)
BOUND_1_PERCENT = 70
BOUND_2_PERCENT = 20
BOUND_3_PERCENT = 10
QUANTUM_TIME = 10
CONTEXT_SWITCH_TIME = 0.001

bound_1_cnt = int(BOUND_1_PERCENT / 100 * PROCESS_CNT)
bound_2_cnt = int(BOUND_2_PERCENT / 100 * PROCESS_CNT)
bound_3_cnt = PROCESS_CNT - (bound_1_cnt + bound_2_cnt)

print("{:d}\n{:d}\n{:d}".format(bound_1_cnt, bound_2_cnt, bound_3_cnt))

p_lst = []
for i in range (0, bound_1_cnt):
    p_lst.append(Process(random.randint(BOUND_1[0], BOUND_1[1])))
for i in range (0, bound_2_cnt):
    p_lst.append(Process(random.randint(BOUND_2[0], BOUND_2[1])))
for i in range (0, bound_3_cnt):
    p_lst.append(Process(random.randint(BOUND_3[0], BOUND_3[1])))

random.shuffle(p_lst)

for i in p_lst:
    print(str(i.run_time), end=' ')

fcfs = FirstComeFirstServe(p_lst)
fcfs_res = fcfs.run()

print(str(fcfs_res.sum_time) + ' ' + str(fcfs_res.avg_wait_time) + ' ' + str(fcfs_res.avg_res_time) + ' ' + str(fcfs_res.avg_turn_around_time))

sjf = ShortestJobFirst(p_lst)
sjf_res = sjf.run()

print(str(sjf_res.sum_time) + ' ' + str(sjf_res.avg_wait_time) + ' ' + str(sjf_res.avg_res_time) + ' ' + str(sjf_res.avg_turn_around_time))

rr = RoundRobin(p_lst, QUANTUM_TIME, CONTEXT_SWITCH_TIME)
rr_res = rr.run()

print(str(rr_res.sum_time) + ' ' + str(rr_res.avg_wait_time) + ' ' + str(rr_res.avg_res_time) + ' ' + str(rr_res.avg_turn_around_time))
