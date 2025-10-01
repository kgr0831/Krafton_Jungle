# https://www.acmicpc.net/problem/11047

_CoinCount, _GoalMoney = map(int, input().split())

_CoinList = []

for _ in range(_CoinCount) :
    coin = int(input())
    if coin <= _GoalMoney :
        _CoinList.append(coin)

def GetCoinCount() :
    leftMoney = _GoalMoney
    count = 0
    _CoinList.reverse()
    
    for coin in _CoinList :
        if leftMoney <= 0 :
            break
        count += leftMoney // coin
        leftMoney = leftMoney % coin

    return count

print(GetCoinCount())
