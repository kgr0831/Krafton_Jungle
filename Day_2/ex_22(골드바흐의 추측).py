# https://www.acmicpc.net/problem/9020
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다.
# 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

import math

inputCount = int(input())

numList = []

for _ in range(inputCount):
    numList.append(int(input()))

def IsPrime(number: int):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1): # 소수 판별 -> 2 ~ number의 제곱근 까지중에 나머지가 0이 없으면 소수
        if number % i == 0:
            return False
    return True


for num in numList :
    count = 0
    for i in range(num // 2, 1, -1): # 시작값 : num / 2, 끝나는 기준 값 : 1, 증가 : -1 //는 정수 나눗셈
        count += 1
        print(count)
        if IsPrime(num - i) and IsPrime(i):
            print(i, num - i)
            break