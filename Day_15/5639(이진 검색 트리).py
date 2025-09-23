# https://www.acmicpc.net/problem/5639
from sys import stdin
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

class Node :
    def __init__(self, kValue, kParent, kChild):
        self.value = kValue
        self.parent = kParent
        self.child = kChild
        if kChild == None :
            self.child = {'Right' : None, 'Left' : None}

    def GetValue(self) :
        return self.value
    
    def GetChild(self) :
        return self.child

    def GetParent(self) :
        return self.parent
    
    def SetChildR(self, kRight) :
        self.child['Right'] = kRight

    def SetChildL(self, kLeft) :
        self.child['Left'] = kLeft

    def CanSetChild(self, kIsLeft : bool) :
        if kIsLeft :
            return self.child['Left'] == None
        else :
            return self.child['Right'] == None

    
rootNode = Node(int(input()), None, None)
treeDict = dict()
treeDict[rootNode.GetValue()] = rootNode

def GetInput(kValue : int, kParent : Node) : 
    if kValue > kParent.GetValue() :
        if kParent.CanSetChild(False) :
            node = Node(kValue, kParent, None) 
            kParent.SetChildR(node)
            treeDict[kValue] = node
        else :
            GetInput(kValue, kParent.GetChild()['Right'])
    else :
        if kParent.CanSetChild(True) :
            node = Node(kValue, kParent, None) 
            kParent.SetChildL(node)
            treeDict[kValue] = node
        else :
            GetInput(kValue, kParent.GetChild()['Left'])
    
    return treeDict[kValue]

def PostOrder(kNode : Node) :
    childs = kNode.GetChild()
    
    if childs['Left'] != None :
        PostOrder(childs['Left'])
    if childs['Right'] != None :
        PostOrder(childs['Right'])
    print(kNode.GetValue())

for line in stdin:
    curTree = GetInput(int(line), rootNode)

PostOrder(rootNode)

# 입력 끝나고 엔터 -> Ctrl + Z -> 엔터