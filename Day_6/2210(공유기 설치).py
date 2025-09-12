# https://www.acmicpc.net/problem/2110
# 도현이의 집 N개가 수직선 위에 있다. 
# 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에,
# 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서,
# 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# region while문 버전

N, C = map(int, input().split())

arr = []
arr.append(int(input()))
for _ in range(N):
    arr.sort()

start = 1 # 공유기 거리 최소
end = arr[-1] - arr[0] # 공유기 거리 최대
result = 0

# 재귀로 적절한 두 공유기 사이의 거리를 찾는다
while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 거리
    current = arr[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(result)

# endregion

# region 다른 버전 -> 재귀

# homeCount, wifiCount = map(int, input().split())

# homePosList = []
# for _ in range(homeCount):
#     homePosList.append(int(input()))

# homePosList.sort()

# def CanSet(dist : int):
#     curPos = homePosList[0]
#     count = 1
#     for i in range(len(homePosList)) :
#         if homePosList[i] - curPos >= dist :
#             count += 1
#             curPos = homePosList[i]
#     return count >= wifiCount

# def GetDist(start, end):
#     if start > end:
#         return end  # 마지막으로 성공한 mid (= 현재 end) 반환
    
#     mid = (start + end) // 2
#     if CanSet(mid): # 가능
#         return GetDist(mid + 1, end) # 거리 키우기
#     else: # 불가능
#         return GetDist(start, mid - 1) # 거리 줄이기
    
# print(GetDist(1, homePosList[-1] - homePosList[0]))

# endregion