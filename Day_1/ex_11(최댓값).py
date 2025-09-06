# https://www.acmicpc.net/problem/2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# region import

from functools import cmp_to_key

#endregion

# region input

indexList = []
for i in range(9):
    indexList.append(int(input()))

# endregion

# region func

def GetNum(): # 가장 큰 수 구하는 함수
    sortList = sorted(indexList, key=cmp_to_key(lambda x, y: (x < y) - (x > y)))
    return sortList[0]

def GetIndex(kNum): # 가장 큰 수의 인덱스 구하는 함수
    index = 1
    for num in indexList:
        if num == kNum : 
            break
        index += 1

    return index

#endregion

# region 실행

print(GetNum())
print(GetIndex(GetNum()))

#endregion