import random
import matplotlib.pyplot as plt
from fcfs import FirstComeFirstServe
from sjf import ShortestJobFirst
from rr import RoundRobin
from process import Process

PROCESS_CNT = 20
BOUND_1 = (2, 8)
BOUND_2 = (20, 30)
BOUND_3 = (35, 40)
BOUND_1_PERCENT = 40
BOUND_2_PERCENT = 40
BOUND_3_PERCENT = 20
QUANTUM_TIME = 10
CONTEXT_SWITCH_TIME = 0.001

bound_1_cnt = int(BOUND_1_PERCENT / 100 * PROCESS_CNT)
bound_2_cnt = int(BOUND_2_PERCENT / 100 * PROCESS_CNT)
bound_3_cnt = PROCESS_CNT - (bound_1_cnt + bound_2_cnt)

p_lst = []
for i in range (0, bound_1_cnt):
    p_lst.append(Process(random.randint(BOUND_1[0], BOUND_1[1])))
for i in range (0, bound_2_cnt):
    p_lst.append(Process(random.randint(BOUND_2[0], BOUND_2[1])))
for i in range (0, bound_3_cnt):
    p_lst.append(Process(random.randint(BOUND_3[0], BOUND_3[1])))

random.shuffle(p_lst)

fcfs = FirstComeFirstServe(p_lst)
fcfs_res = fcfs.run()

sjf = ShortestJobFirst(p_lst)
sjf_res = sjf.run()

rr = RoundRobin(p_lst, QUANTUM_TIME, CONTEXT_SWITCH_TIME)
rr_res = rr.run()

names = ['First Come First Serve', 'Shortest-Job-First', 'Round Robin']
ylim = max(max([fcfs_res.sum_time, sjf_res.sum_time, rr_res.sum_time]),
            max([fcfs_res.avg_wait_time, sjf_res.avg_wait_time, rr_res.avg_wait_time]),
            max([fcfs_res.avg_res_time, sjf_res.avg_res_time, rr_res.avg_res_time]),
            max([fcfs_res.avg_turn_around_time, sjf_res.avg_turn_around_time, rr_res.avg_turn_around_time]))

fig, g = plt.subplots(2, 1)
fig2, g2 = plt.subplots(2, 1)
fig.set_size_inches(10, 12)
fig2.set_size_inches(10, 12)
g[0].set_title('Total Execution Time')
g[0].set_ylabel('Time (ms)')
g[0].set_ylim(0, 1.1 * ylim)
g[0].bar(names, [fcfs_res.sum_time, sjf_res.sum_time, rr_res.sum_time])
g[1].set_title('Average Waiting Time')
g[1].set_ylabel('Time (ms)')
g[1].set_ylim(0, 1.1 * ylim)
g[1].bar(names, [fcfs_res.avg_wait_time, sjf_res.avg_wait_time, rr_res.avg_wait_time], color='r')
g2[0].set_title('Average Response Time')
g2[0].set_ylabel('Time (ms)')
g2[0].set_ylim(0, 1.1 * ylim)
g2[0].bar(names, [fcfs_res.avg_res_time, sjf_res.avg_res_time, rr_res.avg_res_time], color='c')
g2[1].set_title('Average Turn Around Time')
g2[1].set_ylabel('Time (ms)')
g2[1].set_ylim(0, 1.1 * ylim)
g2[1].bar(names, [fcfs_res.avg_turn_around_time, sjf_res.avg_turn_around_time, rr_res.avg_turn_around_time], color='g')
