# https://www.acmicpc.net/problem/1920
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

n_Count = int(input())
n_List = list(map(int, input().split())) # 탐색할 리스트
n_List.sort() # 정렬 -> 바이너리 서치를 위한 거

a_Count = int(input())
a_List = list(map(int, input().split())) # 숫자 리스트

answers = [] # 0,1로 이뤄진 배열 -> 있는지 없는지 저장

for i in range(a_Count) :
    left, right = 0, len(n_List) - 1 # 범위 설정 -> 0 ~ n_List의 길이 - 1
    a_Num = a_List[i] # 목표 -> a_Num -> a_List의 원소
    answers.append(0) # 우선 없음(0)을 저장
    while left <= right : # 끝까지 탐색 
        mid = (left + right) // 2 
        if n_List[mid] == a_Num : # 탐색 완료
            answers[i] = 1
            break
        elif n_List[mid] > a_Num : # 작을 때 -> 오른쪽 범위 축소
            right = mid - 1
        else : # 클 때 -> 왼쪽 범위 축소
            left = mid + 1

for ans in answers:
    print(ans)

# region 다른 버전 => 재귀 함수

# n_Count = int(input())
# n_List = list(map(int, input().split()))
# n_List.sort()

# a_Count = int(input())
# a_List = list(map(int, input().split()))

# def IsIn(left, right, goal):
#     if left > right :
#         return 0
    
#     mid = (left + right) // 2

#     if n_List[mid] == goal :
#         return 1
    
#     elif n_List[mid] > goal :
#         return IsIn(left, mid - 1, goal)
#     else :
#         return IsIn(mid + 1, right, goal)

# for a_Num in a_List :
#     print(IsIn(0, len(n_List) - 1, a_Num))

# endregion

# region 다른 버전 -> set + for

# a_Count = int(input())
# a_List = input().split()

# m_Count = int(input())
# m_List = input().split()


# a_Set = set(a_List) # => 해시 기반 탐색이라 시간복잡도 O(1)
# for m_Num in m_List:
#     print(int(m_Num in a_Set))

# # for m_Num in m_List :
# #     print(int(m_Num in a_List)) => 시간 초과 뜸

#endregion