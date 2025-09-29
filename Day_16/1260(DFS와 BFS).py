# https://www.acmicpc.net/problem/1260
from collections import deque

class Stack :
    def __init__(self):
        self.items = []

    def Pop(self) :
        if len(self.items) > 0 :
            item = self.items[-1]
            del self.items[-1]
            return item
        return None
    
    def Push(self, kValue) :
        self.items.append(kValue)

    def GetLength(self) :
        return len(self.items)

class Node :
    def __init__(self, kValue):
        self.value = kValue
        self.closeNodes = []

    def GetValue(self) :
        return self.value
    
    def AddClose(self, kCloseNode) :
        self.closeNodes.append(kCloseNode)
    
    def GetClose(self, kIndex) :
        if len(self.closeNodes) >= (kIndex + 1) :
            return self.closeNodes[kIndex]
        return None
    
    def GetCloseLenght(self) :
        return len(self.closeNodes)

    def GetAllClose(self) :
        return self.closeNodes

nodeTree = dict()

def GetInput(int_1, int_2) :
    node_1 = nodeTree.get(int_1)
    node_2 = nodeTree.get(int_2)
    if node_1 == None :
        node_1 = Node(int_1)
        nodeTree[int_1] = node_1
    if node_2 == None :
        node_2 = Node(int_2)
        nodeTree[int_2] = node_2
    node_1.AddClose(node_2)
    node_2.AddClose(node_1)

def DFS(kStart : Node) :

    visited = set()
    route = []
    stack = Stack()
    stack.Push(kStart)

    while stack.GetLength() > 0 :
        kNode = stack.Pop()

        if kNode.GetValue() not in visited :
            closeNodeList = sorted(kNode.GetAllClose(), key=lambda x: x.GetValue(), reverse=True)
            for cNode in closeNodeList :
                if cNode.GetValue() not in visited :
                    stack.Push(cNode)
            visited.add(kNode.GetValue())
            route.append(kNode.GetValue())
    
    print(*route)

def BFS(kStart : Node) :
    queue = deque()
    route = []
    visited = set()
    visited.add(kStart.GetValue())
    queue.append(kStart)

    while len(queue) > 0 :
        node = queue.popleft()
        route.append(node.GetValue())
        closeNodeList = sorted(node.GetAllClose(), key=lambda x: x.GetValue())
        for closeNode in closeNodeList :
            if closeNode.GetValue() not in visited : 
                visited.add(closeNode.GetValue())
                queue.append(closeNode)

    print(*route)

def Run(kStartIndex) :
    if nodeTree.get(kStartIndex) != None :
        DFS(nodeTree[kStartIndex])
        BFS(nodeTree[kStartIndex])
    else :
        print(kStartIndex)
        print(kStartIndex)

nodeCount, lineCount, startIndex = map(int, input().split())

for _ in range(int(lineCount)) :
    inputStr = input().split()
    GetInput(int(inputStr[0]), int(inputStr[1]))

Run(startIndex)
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4