class Fifo:
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

    def replace(self):
        mn = self.cur_time
        space = 0
        for i in range(self.frame_size):
            if self.page[i].arrival_time < mn:
                mn = self.page[i].arrival_time
                space = i
        return space

    def run(self, ref_string):
        for string in ref_string:
            cur_index = self.find_page(string)
            if cur_index == -1:
                cur_index = self.find_space()
                if cur_index == -1:
                    cur_index = self.replace()
                    self.page_fault += 1
                self.page[cur_index].valid = False
                self.page[cur_index].physical_address = string
                self.page[cur_index].arrival_time = self.cur_time
                self.cur_time += 1