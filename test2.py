# 주어진 금액을, 사용 가능한 동전 단위를 이용해 얼마나 많은 방법으로 거슬로 줄 수 있는가?

def GetMoney(index : int, coins : int) : 
    if index == -0:
        return 1
    if index < 0 or len(coins) == 0:
        return 0
    return GetMoney(index, coins[1:]) + GetMoney(index - coins[0],coins)

print(GetMoney(3, [1,2,3]))