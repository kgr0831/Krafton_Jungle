# https://www.acmicpc.net/problem/9012

class PsStack :
    def __init__(self):
        self.items = []

    def pop(self) :
        if len(self.items) <= 0 :
            return None
        else :
            item = self.items[-1]
            del self.items[-1]
            return item
    
    def top(self) :
        if len(self.items) <= 0 :
            return None
        else :
            return self.items[-1]

    def push(self, kStr) :
        result = self.top()
        if result != None and  result == "(" and kStr == ")":
            self.pop()
        else :
            self.items.append(kStr)

    def size(self) :
        return len(self.items)


_inputCount = int(input())
_inputStrList = []
_stackList = []

for i in range(_inputCount) :
    _PsStack = PsStack()
    inputStr = input()
    for j in range(len(inputStr)) :
        _PsStack.push(inputStr[j])
    _stackList.append(_PsStack)

for stack in _stackList :
    if stack.size() == 0 :
        print('YES')
    else :
        print('NO')





