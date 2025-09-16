# https://www.acmicpc.net/problem/2630
# 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고,
# 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다.
# 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의
# 하얀색 또는 파란색 색종이를 만들려고 한다.

# region
sizeInput = int(input())
mapPaperList = [list(map(int, input().split())) for _ in range(sizeInput)] # sizeInput번 입력 받기

blueCount = 0
whiteCount = 0

def CutPaper(paperMap):
    color = paperMap[0][0] # 가장 왼쪽 1번의 색을 기준으로 사용
    for row in paperMap: # paperMap 전체 내에 있는 0번 ~ 마지막 열 반복
        for c in row: # 열 내부에 있는 각 셀 반복
            if c != color: # 셀의 색깔이 왼쪽 1번의 기준색과 다르다면 
                return 'Again' # Again -> 다시 쪼개야됨
    return color # 전부 같은 색이면 색을 리턴

def GetIndex(paperMap):
    global blueCount, whiteCount
    result = CutPaper(paperMap)
    if result != 'Again':
        if result == 1:
            blueCount += 1
        else:
            whiteCount += 1
        return

    n = len(paperMap)
    half = n // 2
    # [row[:half] -> row의 왼쪽 절반 가져오기
    # row[half:] -> row의 오른쪽 절반 가져오기
    GetIndex([row[:half] for row in paperMap[:half]])  # 왼쪽 위
    GetIndex([row[half:] for row in paperMap[:half]])  # 오른쪽 위
    GetIndex([row[:half] for row in paperMap[half:]])  # 왼쪽 아래
    GetIndex([row[half:] for row in paperMap[half:]])  # 오른쪽 아래

GetIndex(mapPaperList)
print(whiteCount)
print(blueCount)

#endregion

