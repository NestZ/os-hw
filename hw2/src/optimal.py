class Optimal:
    def __init__(self, frame_size):
        self.frame_size = frame_size
        self.page = []
        self.page_fault = 0
        self.cur_time = 1
        for i in range(frame_size):
            self.page.append(Page())

    def find_space(self):
        for i in range(self.frame_size):
            if self.page[i].valid:
                return i
        return -1

    def find_page(self, addr):
        for i in range(self.frame_size):
            if self.page[i].physical_address == addr:
                return i
        return -1

    def replace(self, ref_string, cur_index):
        mx = 0
        space = 0
        for i in range(self.frame_size):
            cur_mx = len(ref_string)
            for j in range(cur_index, len(ref_string)):
                if ref_string[j] == self.page[i].physical_address:
                    cur_mx = j
                    break
            if cur_mx > mx:
                mx = cur_mx
                space = i
        return space

    def run(self, ref_string):
        for (i, string) in enumerate(ref_string):
            cur_index = self.find_page(string)
            if cur_index == -1:
                cur_index = self.find_space()
                if cur_index == -1:
                    cur_index = self.replace(ref_string, i)
                    self.page_fault += 1
                self.page[cur_index].valid = False
                self.page[cur_index].physical_address = string
                self.page[cur_index].arrival_time = self.cur_time
                self.cur_time += 1