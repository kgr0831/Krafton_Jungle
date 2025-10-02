import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def dfs(idx, total):
    global count
    if idx == N:
        if total == S:
            count += 1
        return
    
    dfs(idx + 1, total + nums[idx])
    dfs(idx + 1, total)

dfs(0, 0)

if S == 0:
    count -= 1

print(count)
