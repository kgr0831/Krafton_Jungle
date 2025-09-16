# https://www.acmicpc.net/problem/10870 
n = int(input())

def GetPibo(index):
    if index <= 1:
        return index
    return GetPibo(index - 1) + GetPibo(index - 2)

print(GetPibo(n))


