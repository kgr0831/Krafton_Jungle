# https://www.acmicpc.net/problem/10872
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def GetFactorial(index : int) :
    if index <= 1:
        return 1
    else :
        return index * GetFactorial(index - 1)
    
print(GetFactorial(int(input())))