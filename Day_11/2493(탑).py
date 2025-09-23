# https://www.acmicpc.net/problem/2493

# region 시간초과 뜸

# # region To-Do

# # 1. 탑의 갯수 받기 => 1 ~ 500,00
# # 2. 탑 크기들 받기 => 1 ~ 100,000,000
# # 3. 탑의 크기를 push 하기
#     # 3-1. 만약 지금 넣는 탑이 처음 이면 결과가 담긴 딕셔너리들을 저장한 리스트에 인덱스와 0을 저장
#     # 3-2. 만약 지금 넣는 탑이 현재 가장 위의 값보다 작다면 결과가 담긴 딕셔너리들(resultDict)을 저장한 리스트(resultDictList)에 인덱스와 스택길이를 저장
#     # 3-3. 만약 지금 넣는 탑이 현재 가장 위의 값보다 크다면 계산 해야하는 딕셔너리들(yetDict)을 저장한 리스트(yetDictList)에 인덱스와 길이를 담기
#     # 3-4. 어떤 딕셔너리 리스트에 저장하는지에 관계없이 길이와 인덱스를 담은 딕셔너리들을 저장한 리스트(self.items)에 저장하기
# # 4. yetDictList의 요소들을 계산 하기
#     # 4-1. for-each로 yetDictList안의 원소 전부 계산 -> 원소 : yetDict
#     # 4-2. yetDict - 1부터 0 까지 -1씩 더하며 반복
#         # 4-2-1. 만약 self.items[i]가 yetDict의 길이 보다 크거나 같다면 yetDict의 인덱스와 i를 저장 & break걸기
#         # 4-2-2. 만약 0까지 안걸리면 yetDict의 인덱스와 0을 저장
# # 5. 결과 출력
#     # 5-1. resultDictList를 'index'순으로 정렬
#     # 5-2. resultDictList -> resultDict의 'result'들을 공백과 함께 출력

# # endregion

# # https://www.acmicpc.net/problem/2493

# # region StackClass

# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def top(self):
#         if len(self.items) <= 0:
#             return -1
#         return self.items[-1]['height']
    
#     def pop(self):
#         if len(self.items) <= 0:
#             return -1
#         item = self.items[-1]
#         del self.items[-1]
#         return item
    
#     def size(self):
#         return len(self.items)

#     def push(self, kHeight):
#         # ✅ push에서는 단순히 쌓기만 한다
#         idx = self.size()
#         self.items.append({'index': idx, 'height': kHeight})

# # endregion


# # region MainLogic

# _inputCount = int(input())  # 1. 탑 개수
# _towerHeightList = list(map(int, input().split()))  # 2. 탑 높이들
# _Stack = Stack()

# # 스택에 모든 탑 넣기 (탐색 X)
# for towerHeight in _towerHeightList:
#     _Stack.push(towerHeight)

# allList = _Stack.items
# resultDictList = []

# # 여기서 한 번에 탐색
# for current in allList:
#     found = 0
#     for i in range(current['index'] - 1, -1, -1):
#         if allList[i]['height'] >= current['height']:
#             found = i + 1  # 백준 2493은 1-based index 출력
#             break
#     resultDictList.append({'index': current['index'], 'result': found})

# # index 순 정렬 (사실 push에서 순서대로 넣었으니 생략 가능)
# resultDictList.sort(key=lambda x: x['index'])

# # 결과 출력
# for result in resultDictList:
#     print(result['result'], end=' ')

# # endregion

# endregion

# To-Do
# 1. 탑 개수를 입력 받음
# 2. 탑의 높이들을 입력 받음
# 3. push 함 -> 현재 push 하려는 값 = (height,index) / 넣는 곳 = leftList = []
    # 3-1. 현재 push 하려는 height와 이전 height들을 비교
        # 3-1-1. 만약 현재 push 하려는 height가 더 크다면 이전의 요소들을 전부 지우고 push -> resultList에 0 추가 
        # 3-1-2. 아니라면 맨 위에 push -> 바로 앞 요소의 result를 resultList에 추가
    # 3-2. 이걸 전체 타워 길이만큼 반복
# 4. 전체 출력

leftList = []
resultList = []

_inputCount = int(input())
_towerHeightList = list(map(int, input().split()))

def push(kTower):
    height, idx = kTower
    
    while leftList and leftList[-1][0] < height:
        leftList.pop()
    
    if leftList:
        resultList.append(leftList[-1][1] + 1)
    else:
        resultList.append(0)
    
    leftList.append((height, idx))

for idx, height in enumerate(_towerHeightList):
    push((height, idx))

print(*resultList)
