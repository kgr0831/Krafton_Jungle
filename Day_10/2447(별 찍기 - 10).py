# https://www.acmicpc.net/problem/2447
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의
# (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
# 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
# TO-DO
# 1. N을 입력 받음
# 2-1. n*n 크기의 공백으로 찬 배열을 만듬
# 2-2. 9개의 영역으로 나눔.
# 2-3. 가운데는 그냥 비우고 다시 나눔
# 2-4. 이제 못나눠서 1이 되면 거기를 *로 채움
# 3. 이제 다 더해서 출력
# region 실패
# n = int(input()) # 1. N을 입력 받음

# totalMap = [[' ' for _ in range(n)] for _ in range(n)] # 2-1. n*n 크기의 공백으로 찬 배열을 만듬
 
# def CutPaper(mapPaper): # 2-2. 9개의 영역으로 나눔.
#     if len(mapPaper) < 3:
#         return None

#     n = len(mapPaper)
#     length = n // 3
#     result = []

#     for i in range(3) : # y
#         for j in range(3) : # x
#             sub = [row[j*length:(j+1)*length] for row in mapPaper[i*length:(i+1)*length]]
#             result.append(sub)

#     return result

# def SplitMap(mapList) :
#     results = CutPaper(mapList)
#     if len(results) == 1 : 
#         results[0][0][0] = '*' # 2-4. 이제 못나눠서 1이 되면 거기를 *로 채움
#     else : # 2-3. 가운데는 그냥 비우고 다시 나눔
#         for i in range(len(results)) :
#             for j in range(len(results[i])) :
#                 if i == 4 : 
#                     continue
#                 CutPaper(results[i][j])

# SplitMap(totalMap)
# print(totalMap)
# endregion
def draw_star(x, y, n): # 시작점 = x, y(0, 0) / 넓이 = n * n (n)
    if n == 1:  # 2-4. 이제 못나눠서 1이 되면 거기를 *로 채움
        totalMap[y][x] = '*' # 2-4. 이제 못나눠서 1이 되면 거기를 *로 채움
        return
    size = n // 3 # 2-2. 9개의 영역으로 나눔.
    for dy in range(3): # 2-2. 9개의 영역으로 나눔.
        for dx in range(3): # 2-2. 9개의 영역으로 나눔.
            if dy == 1 and dx == 1: # 2-3. 가운데는 그냥 비우고 다시 나눔
                continue
            draw_star(x + dx*size, y + dy*size, size)

n = int(input()) # 1. N을 입력 받음
totalMap = [[' ' for _ in range(n)] for _ in range(n)] # 2-1. n*n 크기의 공백으로 찬 배열을 만듬

draw_star(0, 0, n)

for row in totalMap: # 3. 이제 다 더해서 출력
    print("".join(row))

