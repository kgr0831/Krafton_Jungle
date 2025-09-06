# https://www.acmicpc.net/problem/4344
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

inputCount = int(input())
scoresList = []

for _ in range(inputCount) : 
    scoresList.append(
    list(
        map(
            int,input().split()
            )
        )
    )

def GetAverage(kScoreList : list) : 
    totalScore = 0
    scoreCount = kScoreList.pop(0)
    for score in kScoreList:
        totalScore += score
    return totalScore / scoreCount

for scores in scoresList :
    average = GetAverage(scores)
    notAverCount = 0 # 평균 넘는 인원 수
    for score in scores:
        if score > average :
            notAverCount += 1
    percent = (notAverCount / len(scores)) * 100
    print(str(round(percent,3)) + "%")
