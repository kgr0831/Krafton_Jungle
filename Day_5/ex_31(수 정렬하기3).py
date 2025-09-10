# https://www.acmicpc.net/problem/2751
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.


inputCount = int(input())
inputList = []
for _ in range(inputCount) :
    inputList.append(int(input()))

inputList.sort()

for inputData in inputList :
    print(inputData)