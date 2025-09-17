# https://www.acmicpc.net/problem/17608

class StickStack :
    def __init__(self):
        self.items = []

    def pop(self) :
        if len(self.items) <= 0 :
            return -1
        else :
            item = self.items[-1]
            del self.items[-1]
            return item

    def top(self) :
        if len(self.items) <= 0 :
            return -1
        else :
            return self.items[-1]

    def push(self, kData) :
        while self.top() <= kData and self.top() != -1 :
            self.pop()
        self.items.append(kData)

    def size(self) :
        return len(self.items)

_inputCount = int(input())

_StickStack = StickStack()

for _ in range(_inputCount) :
    _StickStack.push(int(input()))

print(_StickStack.size())

# pypy3