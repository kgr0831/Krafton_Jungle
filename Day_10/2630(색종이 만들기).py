# https://www.acmicpc.net/problem/2630
# 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고,
# 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다.
# 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의
# 하얀색 또는 파란색 색종이를 만들려고 한다.

sizeInput = int(input())
mapPaperList = [list(map(int, input().split())) for _ in range(sizeInput)] # sizeInput번 입력 받기

def Cut(paperMap) :
    
    length = len(paperMap) // 2
    mapLength = len(paperMap)

    if mapLength <= 1 :
        return None

    left_1 = []
    for i in range(length) :
        row = []
        for j in range(length) :
            row.append(paperMap[i][j])
        left_1.append(row)

    right_1 = []
    for i in range(length) :
        row = []
        for j in range(length, mapLength) :
            row.append(paperMap[i][j])
        right_1.append(row)

    left_2 = []
    for i in range(length, mapLength) :
        row = []
        for j in range(length) :
            row.append(paperMap[i][j])
        left_2.append(row)

    right_2 = []

    for i in range(length, mapLength) :
        row = []
        for j in range(length, mapLength) :
            row.append(paperMap[i][j])
        right_2.append(row)
    
    return[left_1, left_2, right_1, right_2]


def CanCut(paperMap) : 
    color = paperMap[0][0]
    if len(paperMap) == 1 :
        return color
    
    for i in range(len(paperMap)) :
        for j in range(len(paperMap[i])) :
            if paperMap[i][j] != color :
                return -1
            
    return color

whiteCount = 0
blueCount = 0
def GetIndex(paperMap) :
    global whiteCount
    global blueCount
    result = CanCut(paperMap)
    if result != -1 : # 기저 조건
        if result == 1 :
            blueCount += 1
        else :
            whiteCount += 1
    else :
        cutMaps = Cut(paperMap)
        if cutMaps != None :
            for cutMap in cutMaps : 
                GetIndex(cutMap)

GetIndex(mapPaperList)
print(whiteCount)
print(blueCount)