import heapq
import sys
input = sys.stdin.readline

n = int(input())
lectures = []
for _ in range(n):
    idx, start, end = map(int, input().split())
    lectures.append((start, end, idx))

lectures.sort(key=lambda x: x[0]) # 정렬 -> 시작순서

heap = []
free_rooms = []
room_map = dict()
room_count = 0

for start, end, idx in lectures:
    while heap and heap[0][0] <= start:
        end_time, room_num = heapq.heappop(heap)
        heapq.heappush(free_rooms, room_num)
    
    if free_rooms: # 빈 강의실띠 일때
        room_num = heapq.heappop(free_rooms)
        heapq.heappush(heap, (end, room_num))
        room_map[idx] = room_num
    else: # 아닐 때
        # 새 강의실 개설
        room_count += 1
        heapq.heappush(heap, (end, room_count))
        room_map[idx] = room_count

print(room_count)
for i in range(1, n + 1):
    print(room_map[i])