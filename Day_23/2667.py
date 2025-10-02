# https://www.acmicpc.net/problem/2667


# To-Do
# 1. 지도의 크기 N을 입력받는다.
# 2. N개의 줄에 걸쳐 지도를 입력받아 2차원 리스트에 저장한다.
# 3. 각 좌표를 Node 객체로 변환한다.
    # 3-1. Node의 value는 (좌표, 집 여부)로 저장한다.
    # 3-2. 인접한 상하좌우 집이 있으면 Node의 close 리스트에 연결한다.
# 4. DFS를 이용해 단지를 찾는다.
    # 4-1. 아직 방문하지 않은 집에서 탐색을 시작한다.
    # 4-2. 연결된 모든 집을 방문 처리한다.
    # 4-3. 탐색한 집의 개수를 세어 단지 크기로 기록한다.
# 5. 모든 탐색이 끝나면 단지의 총 개수를 출력한다.
# 6. 단지 크기를 오름차순 정렬하여 출력한다.

# 입력받은 지도에서 집이 있는 칸(1)을 시작점으로
# DFS 탐색을 수행해 연결된 집들을 하나의 단지로 묶고,
# 모든 단지를 탐색해 단지의 총 개수와 각 단지의 크기를 오름차순으로 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Node:
    def __init__(self, kValue):
        """initialize
        
        parameter : value
        """
        self._value = kValue  # (y, x, 집 여부)
        self._close = []

    def SetClose(self, kNode):
        self._close.append(kNode)

    def GetAllClose(self):
        return self._close

    def GetValue(self):
        return self._value

def DFS(node, visited):
    y, x, house = node.GetValue()
    visited[y][x] = True
    count = 1

    for neighbor in node.GetAllClose():
        ny, nx, nh = neighbor.GetValue()
        if not visited[ny][nx] and nh == 1:
            count += DFS(neighbor, visited)
    return count

mapCount = int(input())
board = [list(map(int, input().strip())) for _ in range(mapCount)]

nodes = [[Node((y, x, board[y][x])) for x in range(mapCount)] for y in range(mapCount)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for y in range(mapCount):
    for x in range(mapCount):
        if board[y][x] == 1:
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < mapCount and 0 <= nx < mapCount and board[ny][nx] == 1:
                    nodes[y][x].SetClose(nodes[ny][nx])

visited = [[False] * mapCount for _ in range(mapCount)]
complexSizes = []

for y in range(mapCount):
    for x in range(mapCount):
        if board[y][x] == 1 and not visited[y][x]:
            size = DFS(nodes[y][x], visited)
            complexSizes.append(size)

complexSizes.sort()
print(len(complexSizes))
for size in complexSizes:
    print(size)

