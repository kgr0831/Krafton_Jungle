# https://www.acmicpc.net/problem/10816

sang_Count = int(input())
sang_Card = list(map(int, input().split()))

answer_Count = int(input())
answer_Card = list(map(int, input().split()))

def Merge(left, right) :
    leftIndex = 0
    rightIndex = 0
    result = []
    while leftIndex < len(left) and rightIndex < len(right) :
        if left[leftIndex] <= right[rightIndex] :
            result.append(left[leftIndex])
            leftIndex += 1
        else :
            result.append(right[rightIndex])
            rightIndex += 1
    result += left[leftIndex:]
    result += right[rightIndex:]
    return result

def MergeSort(array):
    if len(array) <= 1:
        return array
    else :
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        sorted_Left = MergeSort(left)
        sorted_Right = MergeSort(right)

        return Merge(sorted_Left, sorted_Right)

sang_Card = MergeSort(sang_Card)

def GetLowIdx(cardNum) :
    left = 0
    right = len(sang_Card)
    while left < right : 
        mid = (left + right) // 2
        if sang_Card[mid] >= cardNum :
            right = mid
        else :
            left = mid + 1
    return left

def GetUpIdx(cardNum) :
    left = 0
    right = len(sang_Card) - 1
    while left < right : 
        mid = (left + right) // 2
        if sang_Card[mid] > cardNum :
            right = mid
        else :
            left = mid + 1
    return left

def GetCardCount(cardNum) :
    return GetUpIdx(cardNum) - GetLowIdx(cardNum)

resultStr = ''
for a_Card in answer_Card :
    resultStr += f'{GetCardCount(a_Card)} '
print(resultStr)