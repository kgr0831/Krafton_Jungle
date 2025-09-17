# https://www.acmicpc.net/problem/10828

# region Stack class

class Stack :
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        if len(self.items) <= 0 :
            return -1
        ite = self.items[-1]
        del self.items[-1]
        return ite
    
    def top(self) :
        if len(self.items) <= 0 :
            return -1
        return self.items[-1]

    def size(self) :
        return len(self.items)
    
    def is_empty(self) :
        return int(len(self.items) == 0)
    
# endregion

commandCount = int(input())

dictList = []

stack = Stack()

def RunCommand(kDict, kIdx) :
    if kDict == 'push' :
        return stack.push(kIdx)
    elif kDict == 'pop' :
        return stack.pop()
    elif kDict == 'size' :
        return stack.size()
    elif kDict == 'empty' :
        return stack.is_empty()
    elif kDict == 'top' :
        return stack.top()

for _ in range(commandCount) : 
    inputList = list(map(str, input().split()))
    commandIdx = None
    if len(inputList) > 1 :
        commandIdx = inputList[1]
    commandStr = inputList[0]
    commandDict = {'commandStr' : commandStr, 'commandIdx' : commandIdx}
    dictList.append(commandDict)

for commandDict in dictList :
    result = RunCommand(commandDict['commandStr'], commandDict['commandIdx'])
    if result != None :
        print(result)