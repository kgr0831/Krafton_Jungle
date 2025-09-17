# https://www.acmicpc.net/problem/10773

class Stack :
    def __init__(self):
        self.items = []

    def pop(self) :
        if len(self.items) <= 0 :
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
    def push(self, kItem) :
        self.items.append(kItem)

_InputCount = int(input())

_Stack = Stack()

for _ in range(_InputCount) :
    inputNum = int(input())
    if inputNum == 0 :
        _Stack.pop()
    else :
        _Stack.push(inputNum)

print(sum(_Stack.items))