# https://www.acmicpc.net/problem/2805
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다.
# 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고,
# 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
# 목재절단기는 다음과 같이 동작한다.
# 먼저, 상근이는 절단기에 높이 H를 지정해야 한다.
# 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다.
# 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
# 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고
# 낮은 나무는 잘리지 않을 것이다.
# 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자.
# 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고,
# 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다.
# (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
# 상근이는 환경에 매우 관심이 많기 때문에,
# 나무를 필요한 만큼만 집으로 가져가려고 한다.
# 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는
# 높이의 최댓값을 구하는 프로그램을 작성하시오.

n_WoodCount, m_Goal = map(int, input().split())
woodList = list(map(int, input().split()))

def GetWoods(woodH): # 자른 나무 양 리턴 함수
    return sum(max(wood - woodH, 0) for wood in woodList)
# sum은 C로 구현되어 있기에 성능적으로 직접 구현 보다 이득

left, right = 0, max(woodList) # => 범위 => 0 ~ 가장 긴 나무 높이
answer = 0 # => 최대 높이 저장용 변수

# 시간 복잡도 = O(N * logH_max) / 공간 복잡도 = O(N) / s.o.f X

while left <= right: # 기저 조건 : left가 right 보다 클 때 => 더 이상 좁힐 범위가 없을 때
    mid = (left + right) // 2 # 탐색 범위 => 중간 부터 시작 => 조건에 따라 범위 좁히기
    if GetWoods(mid) >= m_Goal: # 목표 이상 => 더 높은 높이 탐색
        answer = mid # 답 저장(임시 => 만약에 저게 최대면 저게 답)
        left = mid + 1 # => 최저 높이 높이기 => 구간이 높아짐
    else: # 목표 미달 => 더 낮은 높이 탐색
        right = mid - 1 # => 최대 높이 줄이기 => 구간이 낮아짐

print(answer)

# region 다른 버전 => 재귀 함수

# 시간 복잡도 = O(N * logH_max) / 공간 복잡도 = O(N + log H_max) / s.o.f => 1000번 넘으면

# 각 나무들의 자른 것의 총합을 구해주는 함수
# def GetWoods(woodH):
#     total = 0
#     for wood in woodList:
#         total += max(wood - woodH, 0)
#     return total

# answer = 0
# # 높이 최댓값을 구해주는 함수
# def GetWoodH(left, right):
#     global answer
#     if left > right:
#         return answer
#     mid = (left + right) // 2
#     nowH = GetWoods(mid)
#     if nowH >= m_Goal:
#         answer = mid # 목표 이상이면 mid를 저장
#         return GetWoodH(mid + 1, right) # 더 높은 높이 탐색
#     else:
#         return GetWoodH(left, mid - 1) # 목표 미달이면 더 낮게 탐색
# print(GetWoodH(0, max(woodList)))

#endregion