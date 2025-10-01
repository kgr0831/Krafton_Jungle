import sys

input = sys.stdin.readline

N = int(input())
result = []

for _ in range(N):
    M = int(input())
    applicants = []

    for _ in range(M):
        A, B = map(int, input().split())
        applicants.append((A, B))
    
    applicants.sort(key=lambda x: x[0])

    count = 1
    min_interview = applicants[0][1]

    for i in range(1, M):
        if applicants[i][1] < min_interview:
            count += 1
            min_interview = applicants[i][1]

    result.append(count)

for res in result:
    print(res)

# region 완탐

# https://www.acmicpc.net/problem/1946

# import sys

# input = sys.stdin.readline

# N = int(input())
# result = []
# for _ in range(N):
#     M = int(input())
#     List = []
#     for i in range(M):
#         A,B = map(int, input().split())
#         List.append((A,B))
#     List.sort(key=lambda x:x[0])
#     king = List[0]
#     k2 = []

#     for i in List:
#         if i[1] <= king[1]:
#             k2.append(i)

#     filtered = []
#     for i in k2:
#         is_worse = False
#         for j in k2:
#             if i[0] > j[0] and i[1] > j[1]:
#                 is_worse = True
#                 break
#         if not is_worse:
#             filtered.append(i)

#     k2 = filtered
#     result.append(len(k2))

# for i in result :
#     print(i)

# endregion
