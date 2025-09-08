# https://www.acmicpc.net/problem/1978
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

import math

def IsPrime(number: int):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1): # 소수 판별 -> 2 ~ number의 제곱근 까지중에 나머지가 0이 없으면 소수
        if number % i == 0:
            return False
    return True

inputCount = int(input())
inputs = input().split()

count = 0
for i in range(len(inputs)):
    if IsPrime(int(inputs[i])):
        count += 1

print(count)
