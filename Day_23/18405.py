# https://www.acmicpc.net/problem/18405

# To-Do
# 1. 시험관의 크기(n)와 바이러스 종류(k)를 입력받는다.
# 2. 바이러스들의 위치를 입력받는다.
    # 2-1. node에 바이러스들의 값들과 자신의 좌표를 저장한다.
    # 2-2  node들을 mapList에 저장한다.
    # 2-3. mapList에서 node가 없는 곳에는 None을 저장한다.
    # 2-4. node들만 따로 virusList에 저장한다. -> 2차원 배열로 [k][몇번째 k번 바이러스]
# 3. 바이러스 종류 숫자(k)가 작은 순부터 for문을 통해 반복한다.
    # 3-1. 각node들은 x, y +- 1의 범위의 None이 있는 곳에 node 