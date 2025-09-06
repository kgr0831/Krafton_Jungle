# https://www.acmicpc.net/problem/10869
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
nums = input()
A = int(nums.split(' ')[0])
B = int(nums.split(' ')[1])

print(int(A+B))
print(int(A-B))
print(int(A*B))
print(int(A/B))
print(int(A%B))