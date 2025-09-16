# https://www.acmicpc.net/problem/11401

# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오

# def GetBC(kNum_Top, kNum_Down):
#     if kNum_Down == 0 or kNum_Down == kNum_Top:
#         return 1
#     return GetBC(kNum_Top - 1, kNum_Down - 1) + GetBC(kNum_Top - 1, kNum_Down)  # 파스칼 삼각형 방식
import sys

sys.setrecursionlimit(10 ** 8)

def GetFacto(kNum) :
    if kNum == 1:
        return 1
    else :
        return kNum * GetFacto(kNum - 1)

def GetBCTop(kNum_Top, kCount) :
    if kCount == 0 :
        return 1
    else :
        return kNum_Top * GetBCTop(kNum_Top - 1, kCount - 1)
    
def GetBC(kNum_Top, kNum_Down) :
    return GetBCTop(kNum_Top, kNum_Down) // GetFacto(kNum_Down)

num_Top, num_Down = map(int, input().split())

num = GetBC(num_Top, num_Down)
parametor = 1000000007
if num < parametor : 
    print(num)
else :
    print(num % parametor)
