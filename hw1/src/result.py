class Result:
    def __init__(self, sum_time,
                avg_wait_time = 0,
                avg_res_time = 0,
                avg_turn_around_time = 0):
        self.sum_time = sum_time
        self.avg_wait_time = avg_wait_time
        self.avg_res_time = avg_res_time
        self.avg_turn_around_time = avg_turn_around_time
