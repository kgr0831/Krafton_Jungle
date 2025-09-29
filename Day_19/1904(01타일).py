# https://www.acmicpc.net/problem/1904

import sys
input = sys.stdin.readline

# region 탑 다운

# _CacheDict = dict()
# _CacheDict[1] = 1
# _CacheDict[2] = 2
# def GetCount(kIndex : int) :
#     outPut = _CacheDict.get(kIndex)

#     if outPut != None :
#         return outPut
    
#     result = GetCount(kIndex - 1) + GetCount(kIndex - 2)
#     _CacheDict[kIndex] = result
#     return result

# print(GetCount(int(input())) % 15746)

# endregion

# region 바텀 업

_NCount = int(input())

_CacheArray = [0] * (_NCount + 2)
_CacheArray[1] = 1
_CacheArray[2] = 2
for i in range(3, _NCount + 1) :
   _CacheArray[i] = (_CacheArray[i-1] + _CacheArray[i-2]) % 15746

print(_CacheArray[_NCount])

# endregion