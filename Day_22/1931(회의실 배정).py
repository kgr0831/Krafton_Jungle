# https://www.acmicpc.net/problem/1931

inputCount = int(input())

meetingDataList = []

for _ in range(inputCount) :
    startTime, endTime = map(int, input().split())
    meetingDataList.append((startTime, endTime))

meetingDataList.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 기준, 끝나는 시간이 같으면 시작 시간 기준

count = 0
curTime = 0
for meetingData in meetingDataList :
    if meetingData[0] >= curTime :
        count += 1
        curTime = meetingData[1]

print(count)