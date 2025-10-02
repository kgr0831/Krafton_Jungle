_sCardCount = int(input())
_sCardList = list(map(int, input().split()))

_aCardCount = int(input())
_aCardList = list(map(int, input().split()))

result = ''

_sCardList.sort()

def IsIn(target, left, right) :
    if left > right :
        return '0 '
    
    mid = (left + right) // 2

    if _sCardList[mid] == target :
        return '1 '
    
    if _sCardList[mid] > target :
        return IsIn(target, left, mid - 1)
    else :
        return IsIn(target, mid + 1, right)

for aCard in _aCardList :
    result += IsIn(aCard, 0, len(_sCardList) - 1)
print(result)