# https://www.acmicpc.net/problem/1992
inputCount = int(input())
totalMapList = []

for i in range(inputCount):
    totalMapList.append(list(map(str, input().split())))

def CutMap(mapList):
    mid = len(mapList) // 2
    # mid가 0이면 절대 CutMap 호출하지 않도록 GetCode에서 처리
    t_L_List = [row[:mid] for row in mapList[:mid]]
    t_R_List = [row[mid:] for row in mapList[:mid]]
    d_L_List = [row[:mid] for row in mapList[mid:]]
    d_R_List = [row[mid:] for row in mapList[mid:]]
    return [t_L_List, t_R_List, d_L_List, d_R_List]

def IsFull(mapList):
    num = mapList[0][0]
    for i in range(len(mapList)):
        for j in range(len(mapList[i])):
            if mapList[i][j] != num:
                return None
    return num

def GetCode(kMapList):
    result = IsFull(kMapList)
    if result is not None:  # 모두 같은 값이면 숫자 반환
        return result
    else:
        mapLists = CutMap(kMapList)
        return "(" + GetCode(mapLists[0]) + GetCode(mapLists[1]) + GetCode(mapLists[2]) + GetCode(mapLists[3]) + ")"

print(GetCode(totalMapList))
