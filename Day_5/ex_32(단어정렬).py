# https://www.acmicpc.net/problem/1181
#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.
import sys

input = sys.stdin.readline
inputCount = int(input())
inputList = set()  # 중복 제거

for _ in range(inputCount):
    inputList.add(input().strip())  # \n 제거

# 정렬: 길이 우선, 사전순
inputList = sorted(inputList, key=lambda x: (len(x), x))

for word in inputList:
    print(word)
