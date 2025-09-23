# https://www.acmicpc.net/problem/1991
class Node :
    def __init__(self, kValue, kParent, kLChild, kRChild):
        self.value = kValue
        if kParent == None :
            self.depth = 0
        else :
            self.parent = kParent
            self.depth = kParent.GetDepth() + 1

        self.LChild = kLChild
        self.RChild = kRChild
    
    def GetDepth(self) :
        return self.depth

    def GetValue(self) :
        return self.value

    def GetParent(self) :
        return self.parent
    
    def SetChild(self, kLeft, kRight) :
        self.LChild = kLeft
        self.RChild = kRight
        
    def GetChild(self) :
        return {'left' : self.LChild, 'right' : self.RChild}

treeDict = dict()

rootNodeStr = ''

def GetInput(str_1, str_2, str_3) :
    node_1 = treeDict.get(str_1)
    if node_1 == None :
        node_1 = Node(str_1, None, None, None)
        treeDict[node_1.GetValue()] = node_1
    node_2 = None 
    node_3 = None

    if str_2 != '.' :
        node_2 = Node(str_2, node_1, None, None)
        treeDict[node_2.GetValue()] = node_2

    if str_3 != '.' :
        node_3 = Node(str_3, node_1, None, None)
        treeDict[node_3.GetValue()] = node_3
    
    node_1.SetChild(node_2, node_3)

def PreOrder(kNode : Node) :
    print(kNode.GetValue(), end="")
    child = kNode.GetChild()
    
    if child['left'] != None:
        PreOrder(child['left'])
    if child['right'] != None:
        PreOrder(child['right'])

def InOrder(kNode : Node) :
    child = kNode.GetChild()
    if child['left'] != None:
        InOrder(child['left'])
    print(kNode.GetValue(), end="")
    if child['right'] != None:
        InOrder(child['right'])

def PostOrder(kNode : Node) :
    child = kNode.GetChild()
    if child['left'] != None:
        PostOrder(child['left'])
    if child['right'] != None:
        PostOrder(child['right'])
    print(kNode.GetValue(), end="")

inputCount = int(input())

for i in range(inputCount) :

    inputData =  input().split()
    GetInput(inputData[0], inputData[1], inputData[2])
    if i == 0 :
        rootNodeStr = inputData[0]

PreOrder(treeDict.get(rootNodeStr))
print()
InOrder(treeDict.get(rootNodeStr))
print()
PostOrder(treeDict.get(rootNodeStr))
#print(list(treeDict))