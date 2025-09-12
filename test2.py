n_Count = int(input())
n_List = list(map(int, input().split()))
n_List.sort()

a_Count = int(input())
a_List = list(map(int, input().split()))

def IsIn(left, right, goal):
    if left > right :
        return 0
    
    mid = (left + right) // 2

    if n_List[mid] == goal :
        return 1
    
    elif n_List[mid] > goal :
        return IsIn(left, mid - 1, goal)
    else :
        return IsIn(mid + 1, right, goal)

for a_Num in a_List :
    print(IsIn(0, len(n_List) - 1, a_Num))