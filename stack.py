

class Stack:

    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def par_checker(symbol_string: str) -> bool:
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False

def divid_by_2(decimal:int)->str:
    string=''
    s=Stack()

    while decimal>0:
        rem=decimal%2
        s.push(rem)
        decimal=decimal//2
    
    while not s.is_empty():
        string+=str(s.pop())

    return string

while True:
    s=input('input:')
    print(divid_by_2(int(s)))
