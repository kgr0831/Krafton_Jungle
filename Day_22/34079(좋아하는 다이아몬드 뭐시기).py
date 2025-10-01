# https://www.acmicpc.net/problem/34079

import sys              # 시스템 입출력 관련 모듈
from collections import deque  # BFS를 위한 큐 자료구조
input = sys.stdin.readline      # 빠른 입력 함수

# 장소 수(n)와 도로 수(m) 입력
n, m = map(int, input().split())

# 그래프 인접리스트 초기화 (1-based index)
graph = [[] for _ in range(n+1)]

# 도로 정보 입력 및 그래프 양방향 간선 추가
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  # u에서 v로 이동 가능
    graph[v].append(u)  # v에서 u로 이동 가능

# BFS 수행하며 각 노드까지 최단 거리와 최단 경로 개수 계산
def bfs_count_paths(start):
    dist = [-1] * (n+1)     # 거리 초기화 (-1: 방문 안함)
    count = [0] * (n+1)     # 최단 경로 개수 초기화
    q = deque([start])      # BFS용 큐 생성
    dist[start] = 0         # 시작 노드 거리 0
    count[start] = 1        # 시작 노드 경로 개수 1

    while q:                # 큐가 빌 때까지 반복
        u = q.popleft()     # 현재 노드 꺼내기
        for v in graph[u]:  # 현재 노드의 모든 인접 노드 탐색
            if dist[v] == -1:          # 아직 방문하지 않은 경우
                dist[v] = dist[u] + 1 # 거리 갱신
                count[v] = count[u]   # 최단 경로 개수 갱신
                q.append(v)           # 큐에 추가
            elif dist[v] == dist[u] + 1: # 이미 방문했지만 최단 경로 발견
                count[v] += count[u]    # 최단 경로 개수 누적
    return dist, count                    # 각 노드 거리와 최단 경로 개수 반환

# 1번(학교)에서 각 노드까지 BFS 수행
dist_start, cnt_start = bfs_count_paths(1)

# n번(다이아몬드 집)에서 각 노드까지 BFS 수행
dist_end, cnt_end = bfs_count_paths(n)

# 1에서 n까지 총 최단 경로 개수
total_paths = cnt_start[n]

found = False   # 항상 만나는 노드 발견 여부

# 후보 노드 탐색 (학교와 집 제외)
for v in range(2, n):
    # 최단 경로에 포함되고 모든 최단 경로에 존재하는 경우
    if dist_start[v] + dist_end[v] == dist_start[n] and cnt_start[v] * cnt_end[v] == total_paths:
        print(v)   # 후보 노드 출력
        found = True
        break      # 첫 번째 후보만 출력하고 종료

# 후보 없으면 1 출력 (학교에서 만남)
if not found:
    print(1)
