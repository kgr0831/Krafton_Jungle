# https://www.acmicpc.net/problem/2606

class Node :
    def __init__(self, kValue) :
        """initialize
        
        parameter : value
        """
        self._value = kValue
        self._close = []

    def SetClose(self, kNode) :
        self._close.append(kNode)

    def GetClose(self, kIndex) :
        if len(self._close) >= (kIndex + 1) :
            return self._close[kIndex]
        return None
    
    def GetAllClose(self) :
        return self._close
    
    def GetValue(self) :
        return self._value

class Stack :
    def __init__(self):
        """initialize
        
        parameter : None
        """
        self._items = []

    def Push(self, kItem) :
        self._items.append(kItem)
    
    def Pop(self) :
        if len(self._items) > 0 :
            item = self._items[-1]
            del self._items[-1]
            return item
        return None
    
    def GetLength(self) :
        return len(self._items)

    def Clear(self) :
        self._items.clear()

treeDict = dict()

def GetInput(kValue_1, kValue_2) :
    node_1 = treeDict.get(kValue_1)
    if node_1 is None :
        node_1 = Node(kValue_1)
        treeDict[kValue_1] = node_1

    node_2 = treeDict.get(kValue_2)
    if node_2 is None :
        node_2 = Node(kValue_2)
        treeDict[kValue_2] = node_2
    
    node_1.SetClose(node_2)
    node_2.SetClose(node_1)


def DFSCount(kStart : Node) :
    if kStart is None :
        return 0
    stack = Stack()
    visited = set()
    visited.add(kStart.GetValue())
    stack.Push(kStart)

    while stack.GetLength() > 0 :
        focusNode = stack.Pop()

        closeNodeList = focusNode.GetAllClose()
        for closeNode in closeNodeList :
            if closeNode.GetValue() not in visited :
                visited.add(closeNode.GetValue())
                stack.Push(closeNode)

    return len(visited) - 1


computerCount = int(input())
pareCount = int(input())

for _ in range(pareCount) :
    value_1, value_2 = map(int, input().split())
    GetInput(value_1, value_2)

print(DFSCount(treeDict.get(1)))