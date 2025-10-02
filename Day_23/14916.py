# https://www.acmicpc.net/problem/14916

_goalMoney = int(input())

_Count = 0
_leftMoney = _goalMoney
_Coins = [5,2]

if _goalMoney < 2 or _goalMoney == 3 : # 못 거슬러주는 경우 -> 3이나 2미만
    print(-1)
else :
    for coin in _Coins :
        count = _leftMoney // coin
        # 짝 홀수 보정 미안합니다 조건문이 좀 길죠 ㅠㅠ
        # 만약 짝수라면? -> -5 * 짝수만큼 
        # 만약 홀수라면? -> -5 * 홀수만큼
        if (_leftMoney % 2 == 0 and coin % 2 != 0 and count % 2 != 0) or _leftMoney % 2 != 0 and coin % 2 != 0 and count % 2 == 0: 
            count = (_leftMoney // coin) - 1
            _leftMoney = _leftMoney - (coin * count)
        else :
            _leftMoney = _leftMoney % coin
        _Count += count

    print(_Count)