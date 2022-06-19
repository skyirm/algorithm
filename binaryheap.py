class Bianryheap:

    def __init__(self) -> None:
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i //
                                                  2] = self.heap_list[i//2], self.heap_list[i]
            i = i//2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def min_child(self, i):
        if 2*i+1 > self.current_size:
            return 2*i
        if self.heap_list[2*i] < self.heap_list[2*i+1]:
            return 2*i
        else:
            return 2*i+1

    def perc_down(self, i):
        while (2*i) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def del_min(self):
        minval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return minval

    def build_heap(self, alist: list):
        i = len(alist)
        self.current_size = len(alist)
        self.heap_list = [0]+alist
        while i > 0:
            self.perc_down(i)
            i -= 1

if __name__ == "__main__":
    alist=[13, 421, 41, 51, 51, 345, 636, 2, 6, 36, 0]
    heap=Bianryheap()
    heap.build_heap(alist)
    print(heap.heap_list)
    heap.del_min()
    print(heap.heap_list)