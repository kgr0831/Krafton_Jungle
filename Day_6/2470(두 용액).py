# https://www.acmicpc.net/problem/2470

# KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.
# 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.
# 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고,
# 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
# 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
# 예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는
# 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고,
# 이 용액이 특성값이 0에 가장 가까운 용액이다.
# 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로
# 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
# 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때,
# 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을
# 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

# region while 버전1

# inputCount = int(input())
# inputNumList = list(map(int, input().split()))

# inputNumList.sort()

# result = float('inf') # inf => 값 = 무한
# lIndex, rIndex = 0, inputCount - 1 # 왼쪽 -> 0 / 오른쪽 -> 최대 인덱스 
# resultLeft, resultRight = 0, 0  # 최종 정답 인덱스

# # 탐색 범위 : 전체
# while lIndex < rIndex: # (이진 탐색 -> 완전 탐색) = 파라메트릭 서치(매개변수 탐색, parametric search)
#     sumNum = inputNumList[lIndex] + inputNumList[rIndex]
#     if abs(sumNum) < abs(result): # sumNum이 result보다 0에 가까우면
#         result = sumNum # 정답을 sumNum으로 교체
#         resultLeft, resultRight = lIndex, rIndex # 정답 인덱스를 sumNum으로 교체

#     if sumNum < 0: # sumNum이 음수
#         lIndex += 1 # 음수 방향 값 낮추기
#     else: # sumNum이 양수
#         rIndex -= 1 # 양수 방향 값 낮추기

# print(inputNumList[resultLeft], inputNumList[resultRight]) 

# endregion

# region 재귀 버전

# import sys
# sys.setrecursionlimit(10**6) # 재귀 스택 제한 해제

# inputCount = int(input())
# NumList = list(map(int, input().split()))
# NumList.sort()  # 정렬 필수

# def GetIndex(kLeft, kRight, best_sum, best_pair):
#     if kLeft >= kRight:  # 종료 조건 => 탐색 끝날때까지
#         return best_pair # 이전 kLeft + kRight

#     sumNum = NumList[kLeft] + NumList[kRight]

#     if abs(sumNum) < abs(best_sum): # sumNum이 현재 best_sum 보다 0에 더 근접 할 때
#         best_sum = sumNum # best_sum 교체
#         best_pair = (kLeft, kRight) # best pair 교체

#     if sumNum > 0: # 양수 일 때
#         return GetIndex(kLeft, kRight - 1, best_sum, best_pair) # kRight 줄이기
#     else: # 음수 일 때
#         return GetIndex(kLeft + 1, kRight, best_sum, best_pair) # kLeft 줄이기

# result_pair = GetIndex(0, inputCount - 1, float("inf"), (0, 0))
# print(NumList[result_pair[0]], NumList[result_pair[1]])

# endregion

# region 재귀 버전2

import sys
sys.setrecursionlimit(10**6) # 재귀 스택 제한 해제

inputCount = int(input())
numList = list(map(int, input().split()))

numList.sort()

def GetIndex(kLeft, kRight, kBSum, kBPair):
    if kLeft >= kRight :
        return kBPair
    
    sumNum = numList[kLeft] + numList[kRight]

    if abs(kBSum) > abs(sumNum) :
        kBSum = sumNum
        kBPair = (kLeft, kRight)
    
    if sumNum > 0:
        return GetIndex(kLeft, kRight - 1, kBSum, kBPair)
    else :
        return GetIndex(kLeft + 1, kRight, kBSum, kBPair)
    
indexList = GetIndex(0, len(numList) - 1, float('inf'), (0,0))
print(numList[indexList[0]], numList[indexList[1]])

# endregion