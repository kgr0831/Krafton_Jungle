# https://www.acmicpc.net/problem/10950
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

inputCount = int(input()) # input 받는 갯수
input_Fronts = []
input_Backs = []

for i in range(inputCount) :
    inputIndex = input().split(' ')
    input_Fronts.append(int(inputIndex[0]))
    input_Backs.append(int(inputIndex[1]))

for i in range(len(input_Fronts)) :
    print(input_Fronts[i] + input_Backs[i])