# https://www.acmicpc.net/problem/1780
# N×N크기의 행렬로 표현되는 종이가 있다.
# 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
# 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고,
# 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때,
# -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수,
# 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

from itertools import product

iter = [1,2,3,4]
for i in product(iter, repeat=2):
    print(i)

# yCount = int(input())

# mapList = []

# for _ in range(yCount) : 
#     mapList.append(list(map(int, input().split())))
# count_List = [0,0,0]

def CanCut(mapPaper) :
    num = mapPaper[0][0]
    length = len(mapPaper)
    for i in range(length) :
        for j in range(length) :
            if mapPaper[i][j] != num :
                return None
    return num

def CutPaper(mapPaper) :
    if len(mapPaper) < 3 :
        return None

    length = len(mapPaper) // 3
    result = []
    list_1 = []
    for i in range(length) :
        list_Row = []
        for j in range(length) :
            list_Row.append(mapPaper[i][j]) # 1, 1
        list_1.append(list_Row)
    result.append(list_1)
    
    list_2 = []
    for i in range(length, length * 2) :
        list_Row = []
        for j in range(length) :
            list_Row.append(mapPaper[i][j]) # 2, 1
        list_2.append(list_Row)
    result.append(list_2)
    
    list_3 = []
    for i in range(length * 2, length * 3) :
        list_Row = []
        for j in range(length) :
            list_Row.append(mapPaper[i][j]) # 3, 1
        list_3.append(list_Row)
    result.append(list_3)

    list_4 = []
    for i in range(length) :
        list_Row = []
        for j in range(length, length * 2) :
            list_Row.append(mapPaper[i][j]) # 1, 2
        list_4.append(list_Row)
    result.append(list_4)
    
    list_5 = []
    for i in range(length, length * 2) :
        list_Row = []
        for j in range(length, length * 2) :
            list_Row.append(mapPaper[i][j]) # 2, 2
        list_5.append(list_Row)
    result.append(list_5)
    
    list_6 = []
    for i in range(length * 2, length * 3) :
        list_Row = []
        for j in range(length, length * 2) :
            list_Row.append(mapPaper[i][j]) # 3, 2
        list_6.append(list_Row)
    result.append(list_6)

    list_7 = []
    for i in range(length) :
        list_Row = []
        for j in range(length * 2, length * 3) :
            list_Row.append(mapPaper[i][j]) # 1, 3
        list_7.append(list_Row)
    result.append(list_7)
    
    list_8 = []
    for i in range(length, length * 2) :
        list_Row = []
        for j in range(length * 2, length * 3) :
            list_Row.append(mapPaper[i][j]) # 2, 3
        list_8.append(list_Row)
    result.append(list_8)
    
    list_9 = []
    for i in range(length * 2, length * 3) :
        list_Row = []
        for j in range(length * 2, length * 3) :
            list_Row.append(mapPaper[i][j]) # 3, 3
        list_9.append(list_Row)
    result.append(list_9)

    return result

def GetCount(mapPaper) :
    global count_List
    result_CanCut = CanCut(mapPaper)
    if len(mapPaper) == 1 or result_CanCut != None:
        idx = result_CanCut + 1
        count_List[idx] += 1
    else :
        results = CutPaper(mapPaper)
        if results != None :
            for result in results :
                GetCount(result)


# GetCount(mapList)
# for count in count_List :
#     print(count)