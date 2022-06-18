

class Queue:

    def __init__(self) -> None:
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotpotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotpotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 5))