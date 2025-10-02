# # https://www.acmicpc.net/problem/1338

# To-Do
# 1. 세로, 가로 크기를 입력받는다.
# 2. 행들을 입력받아 mapList에 저장한다.
# 3. - 판자 세기
    # 3-1. 각 행을 차례대로 돈다.
    # 3-2. -를 만나면 연속된 -가 끝날 때까지 건너뛰고 1개만 카운트한다.
# 4. | 판자 세기
    # 4-1. 각 열을 차례대로 돈다.
    # 4-2. |를 만나면 연속된 |가 끝날 때까지 건너뛰고 1개만 카운트한다.
# 5. 두 카운트를 합쳐 출력한다.

# 입력받은 바닥 장식을 행과 열 단위로 확인하면서,
# 연속된 '-'는 하나의 가로 판자로,
# 연속된 '|'는 하나의 세로 판자로 취급해 개수를 세고 합산하여 출력한다.

import sys
input = sys.stdin.readline

ySize, xSize = map(int, input().split())
board = [list(input().strip()) for _ in range(ySize)]

count = 0

for y in range(ySize) :
    x = 0
    while x < xSize :
        if board[y][j] == '-' :
            count += 1
            while x < xSize and board[y][x] == '-' :
                x += 1
        else :
            j += 1

for j in range(xSize) :
    i = 0
    while i < ySize :
        if board[i][j] == '|' :
            count += 1
            while i < ySize and board[i][j] == '|' :
                i += 1
        else :
            i += 1

print(count)