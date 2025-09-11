# https://www.acmicpc.net/problem/1920
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# a_Count = int(input())
# a_List = input().split()

# m_Count = int(input())
# m_List = input().split()


# a_Set = set(a_List) # => 해시 기반 탐색이라 시간복잡도 O(1)
# for m_Num in m_List:
#     print(int(m_Num in a_Set))

# # for m_Num in m_List :
# #     print(int(m_Num in a_List)) => 시간 초과 뜸
a_Count = int(input())
a_List = list(map(int, input().split()))
a_List.sort()

m_Count = int(input())
m_List = list(map(int, input().split()))

def binary_search(left, right, goal):
    if left > right:
        return False
    
    mid = (left + right) // 2
    
    if goal == a_List[mid]:
        return True
    elif goal > a_List[mid]:
        return binary_search(mid + 1, right, goal)
    else:
        return binary_search(left, mid - 1, goal)

for m in m_List:
    print(1 if binary_search(0, a_Count - 1, m) else 0)
