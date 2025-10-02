from itertools import combinations

class userInfo:
    def __init__(self, kName, kIndex, kLine, kTier):
        self._Name = kName
        self._Index = kIndex
        self._Line = kLine
        self._Tier = kTier

tierDict = {
    "아이언": 0, 
    "브론즈": 400,
    "실버": 800,
    "골드": 1200,
    "플레티넘": 1600,
    "에메랄드": 2000,
    "다이아몬드": 2400,
    "마스터": 2800,
    "그랜드마스터": 2800,
    "챌린저": 2800
}

tierGradeDict = {
    "4": 0,
    "3": 100,
    "2": 200,
    "1": 300
}

def GetPowerScore(tierName, tierGrade, tierPoint):
    if tierDict[tierName] >= 2800:  # 마스터 이상
        return tierDict[tierName] + int(tierPoint)
    return tierDict[tierName] + tierGradeDict[tierGrade] + int(tierPoint)

def GetAllPoint(players):
    score = 0
    for user in players:  # iterable (list, tuple, set 모두 가능)
        score += user._Tier
    return score

# ====== 입력 ======
inputCount = int(input())
userList = []

for i in range(inputCount):
    name, line, tierName, tierGrade, tierPoint = map(str, input().split())
    tier = GetPowerScore(tierName, tierGrade, tierPoint)
    userList.append(userInfo(name, i, line, tier))

print("================================")

# ====== 팀 나누기 ======
balancedTeams = list(combinations(userList, 5))
teamTuples = []

for i in range(len(balancedTeams)):
    team = balancedTeams[i]
    opponent = set(userList) - set(team)
    diff = abs(GetAllPoint(team) - GetAllPoint(opponent))
    teamTuples.append((diff, i))

teamTuples.sort(key=lambda x: x[0])

bestTeam = balancedTeams[teamTuples[0][1]]
opponentTeam = list(set(userList) - set(bestTeam))

# ====== 출력 ======
print("=== 팀 A ===")
for u in bestTeam:
    print(u._Name, end =" ")

print("\n=== 팀 B ===")
for u in opponentTeam:
    print(u._Name, end =" ")

