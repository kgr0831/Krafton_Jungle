# https://www.acmicpc.net/problem/11724

# To-Do
# 1. 노드의 개수와 선의 개수를 입력 받는다.
# 2. 선의 개수 만큼 이어진 노드들을 받는다. -> 1번 입력 노드와 2번 입력 노드
# 3. 만약 1번 입력노드나 2번 입력 노드가 전체 노드 스택에 없다면, 노드 클래스를 생성하고 그 클래스를 스택에 넣는다.
#     3-1. 서로 클래스에 인접 노드 정보를 저장한다.
# 4. 전체 노드가 담긴 스택에서 반복문을 통해 개수를 구한다.
#     4-1. 빈 해시테이블(dict)를 만든다.
#         4-1-1. 스택에서 요소 하나를 pop해온다.
#         4-1-2. pop 한 요소를 해시테이블에 넣는다.
#         4-1-3. pop한 요소의 인접노드로 같은 과정을 반복한다.
#         4-1-4. 모든 인접노드가 이미 다 해시테이블에 있다면 종료한다.
#     4-2. 카운트(int변수)를 1더하고 4-1의 과정들을 스택의 길이가 0이 될때 까지 반복한다.
# 5. 카운트를 출력한다.

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

class Node :
    def __init__(self, kValue):
        self.value = kValue
        self.closeNodeList = []

    def GetAllClose(self) :
        return self.closeNodeList
    
    def GetClose(self, kIndex = 0) :
        if len(self.closeNodeList) >= (kIndex + 1) :
            return self.closeNodeList[kIndex]
        return None
    
    def SetClose(self, kNode) :
        self.closeNodeList.append(kNode)

    def GetValue(self) :
        return self.value

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

_nodeDict = dict()
_nodeStack = Stack()

def GetInput(kValue_1, kValue_2) :
    node_1 = _nodeDict.get(kValue_1)
    if node_1 is None : 
        node_1 = Node(kValue_1)
        _nodeDict[kValue_1] = node_1
        _nodeStack.Push(node_1)
        
    node_2 = _nodeDict.get(kValue_2)
    if node_2 is None :
        node_2 = Node(kValue_2)
        _nodeDict[kValue_2] = node_2
        _nodeStack.Push(node_2)

    node_1.SetClose(node_2)
    node_2.SetClose(node_1)

visited = set()

def DFS(kNode : Node) :
    if kNode.GetValue() not in visited :
        visited.add(kNode.GetValue())
    closeNodeList = kNode.GetAllClose()

    for closeNode in closeNodeList :
        if closeNode.GetValue() not in visited :
            DFS(closeNode)

def GetCount() :
    count = 0
    for node in _nodeDict.values():
        if node.GetValue() not in visited:
            DFS(node) 
            count += 1
    return count

_NodeCount, _LineCount = map(int, input().split())

for _ in range(_LineCount):
    value_1, value_2 = map(int, input().split())
    GetInput(value_1, value_2)

for i in range(1, _NodeCount + 1):
    if i not in _nodeDict:
        node = Node(i)
        _nodeDict[i] = node
        _nodeStack.Push(node)

print(GetCount())