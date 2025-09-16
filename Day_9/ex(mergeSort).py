# merge sort를 통한 분할 정복 연습

# 분할정복 관점에서 머지소트 구조
# 1. Divide (쪼개기)
#   배열을 반으로 나눔
#   왼쪽 절반, 오른쪽 절반 각각 재귀 호출
# 2. Conquer (작은 문제 해결)
#   배열 크기가 1이면 이미 정렬된 상태 → 그대로 반환
#   크기가 2 이상이면 재귀로 왼쪽/오른쪽 정렬
# 3. Combine (합치기)
#   정렬된 왼쪽 배열과 오른쪽 배열을 하나씩 비교하면서 새로운 배열로 합치기


numList = [9,3,6,2,10,4,5,7,0,8,1]

def MergeSort(array):
    if len(array) <= 1 :
        return array
    
    mid = len(array) // 2 # 절반 정하기
    left = array[:mid] # 좌우 나누기
    right = array[mid:] # 좌우 나누기

    sorted_Left = MergeSort(left)
    sorted_Right = MergeSort(right)

    return merge(sorted_Left, sorted_Right)

def merge(left, right):
    # left와 right를 비교하면서 하나의 정렬된 배열로 합치기
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else :
            result.append(right[rightIndex])
            rightIndex += 1
    # for i in range(len(left) - leftIndex, len(left)) : 
    #     result.append(left[i])
    # for i in range(len(right) - rightIndex, len(right)) : 
    #     result.append(right[i])
    # 아래 같이 요약 가능
    result += left[leftIndex:]
    result += right[rightIndex:]

    return result

print(MergeSort(numList))