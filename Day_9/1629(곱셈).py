# https://www.acmicpc.net/problem/1629
# 자연수 A를 B번 곱한 수를 알고 싶다.
# 단 구하려는 수가 매우 커질 수 있으므로
# 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())

def power(a, b):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result

print(power(a, b))