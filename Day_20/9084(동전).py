# https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

def GetCaseCount(kCoinList : list, kMoney : int) -> int : 
    dp = [0] * (kMoney + 1)
    dp[0] = 1
    for coin in kCoinList :
        for i in range(coin, kMoney + 1) :
            dp[i] += dp[i - coin]
            
    return dp[kMoney]

_InputCount = int(input())
results = []
for _ in range(_InputCount) :
    coinCount = int(input())
    coinList = list(map(int, input().split()))
    money = int(input())
    results.append(GetCaseCount(coinList, money))

for result in results :
    print(result)