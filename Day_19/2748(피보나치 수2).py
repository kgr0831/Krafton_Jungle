# https://www.acmicpc.net/problem/2748

# region 탑 다운 방식
# cacheDict = dict()

# def Fibo(kIndex : int) :
#     if kIndex < 3 :
#         return 1
#     cacheData = cacheDict.get(kIndex)
#     if cacheData != None :
#         return cacheData
#     cacheDict[kIndex] = Fibo(kIndex - 1) + Fibo(kIndex - 2)
#     return cacheDict[kIndex]

# print(Fibo(int(input())))

# endregion

# region 보텀업 방식

cacheDict = dict()

def Fibo(kIndex) :
    if kIndex < 3 :
        return 1
    
    cacheDict[1] = 1
    cacheDict[2] = 1

    for i in range(3, kIndex + 1) : 
        cacheDict[i] = cacheDict[i - 1] + cacheDict[i - 2]

    return cacheDict[kIndex]

print(Fibo(int(input())))

# endregion

