# https://www.acmicpc.net/problem/10871
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

inputStrs = input().split(' ')
reqIndex = int(inputStrs[1])

indexList = input().split(' ')


outStr = ""
for index in indexList :
    if reqIndex > int(index) :
        outStr += f"{index} "

print(outStr)