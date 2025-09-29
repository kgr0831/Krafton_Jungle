# https://www.acmicpc.net/problem/11053
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# region for문 버전

inputCount = int(input()) # 6
numList = list(map(int, input().split())) # 10, 20, 10, 30, 20, 50

lis_lengths = [1] * inputCount # 1, 1, 1, 1, 1, 1

for i in range(inputCount): # 6 번 반복
    for j in range(i): # 0 ~ 5 번 반복
        if numList[j] < numList[i]:
            lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

print(max(lis_lengths))

# endregion