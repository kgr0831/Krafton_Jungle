# https://www.acmicpc.net/problem/1300
# 세준이는 크기가 N×N인 배열 A를 만들었다.
# 배열에 들어있는 수 A[i][j] = i×j 이다.
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다.
# B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 배열 A와 B의 인덱스는 1부터 시작한다.

sizeIndex = int(input())
goalNum = int(input())
array = []

for i in range(1, sizeIndex + 1):
    for j in range(1, sizeIndex + 1):
        array.append(i * j)
        
def GetIndex(indexRange_L: int, indexRange_R : int) :
    if indexRange_L > indexRange_R:
        return '없음'
    mid = (indexRange_L + indexRange_R) // 2
    if array[mid] == goalNum:
        return mid
    elif array[mid] > goalNum:
        return GetIndex(indexRange_L, mid - 1)
    else:
        return GetIndex( mid + 1, indexRange_R)
    
# def binary_search(arr, target): -> 재귀에 비해 가독성은 떨어지지만 성능과 안정성이 오름
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return '없음'
    
print(GetIndex(0, len(array) - 1))