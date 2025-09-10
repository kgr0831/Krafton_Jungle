
# 306호
# 1. 파이썬에서 문자열 데이터를 "문자열(str)"로 관리하는 것과 각각의 문자를 "배열(list)"로 관리하는 것의 장단점은 무엇일까?

# 답 : 문자열은 한번 생성하면 바꿀 수 없지만, 길이가 정해지게 되고 같은 값을 가진 문자열을 재사용하기에 공간복잡도가 낮아진다.

# 리스트로 관리한다면 길이가 정해져 있지 않기에, 문자 하나하나를 바꿀수 있지만, 길이가 정해져있지 않으니까 공간복잡도가 높아진다.

# 2.아래 코드의 실행 결과를 예측하시오.

# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()

# message3()

# 답 : BCBCBCA

# 3. 다음 코드의 출력 결과를 예측하고, 왜 그렇게 되는지 각각 설명하시오.

# def modify(a, b, c):
#     a += 1
#     b.append(4)
#     c = [100, 200]

# x = 10
# y = [1, 2, 3]
# z = [7, 8, 9]

# modify(x, y, z)

# print(x) # (1)
# print(y) # (2)
# print(z) # (3)

# 답 : 10
# [1, 2, 3]
# [7, 8, 9]
# call by value이기 때문

# 4. 인덱스를 이용해서 배열의 특정 값을 읽을 때 시간 복잡도를 빅오 표기법으로 기입하라. 또한 정답의 이유를 설명하라.

# 답 : O(1) / RAM은 랜덤 엑세스가 가능하고, 배열 생성시에 배열의 시작점 주소와 길이를 저장해 놓아서 인덱스를 안다면 주소가 특정되기에 바로 엑세스 할 수 있기 때문이다.

# 5. 다음의 코드는 팩토리얼을 구하는 재귀함수이다. 빈 칸을 채워 완성 하시오. 

# def factorial(n):
#    if n <= 1:
#        return 1
#    return __________

# 답 : n * factorial(n - 1)

# 6. 한 절에 여러 스님들이 살고 있다. 스님들은 매일 아침 모여 서로의 얼굴을 볼 수 있지만, 자신의 얼굴은 볼 수 없다. 어느 날, 주지 스님이 이렇게 말했다.
# “이 절에 병에 걸린 스님들이 있다. 병에 걸린 스님은 머리에 붉은 점이 생긴다. 본인이 병에 걸렸다는 사실을 알게 되는 즉시, 절을 떠나야 한다.”
# 그날 이후 병에 걸린 스님들은 매일 아침 서로의 얼굴을 확인했지만, 1일부터 6일까지는 아무도 절을 떠나지 않았다.
# 그러나 7일째 아침, 병에 걸린 스님들이 모두 동시에 절을 떠났는지 자취를 감추었다. 이때, 병에 걸린 스님의 수는 몇 명이었을까? 답을 구하고 이를 재귀 함수로 만들어라.
# (단, 주지 스팀이 떠나라고 한 날은 0일 차며 0일차부터 마지막 날까지 병에 걸린 스님의 수는 변하지 않았다. 주지 스님은 병에 걸리지 않았다.)

# 답 : 모르겠어요

# 7. 캐시 메모리를 사용하면 컴퓨터 시스템의 성능이 왜 향상되는지 지역성(locality) 개념을 포함하여 설명하시오.

# 답 : 캐시 메모리는 SRAM을 사용하고, 이 SRAM의 속도는 DRAM보다 100배가까이 빠른데, 캐시 메모리는 자주 사용하는 인스트럭션들을 캐시로 SRAM에 저장하는 것이기 때문에 자주 사용하는 인스트럭션들을 DRAM의 100배에 가까운 속도로 전달하기에 CPU의 속도에 비해 크게 늦지 않아 병목현상을 줄일수 있기 때문이다. 

# 8. 유닉스(Unix) 계열 시스템은 POSIX라는 공통 표준을 따른다. 운영체제에 이러한 표준이 필요한 이유에 대해, 본인의 생각을 중심으로 서술하시오.
#  (표준의 역할, 개발자/사용자 관점, 시스템 호환성 등 다양한 측면에서 접근해도 좋습니다.)

# 답 : 모르겠어요

# 9. 브라우저에서 여러 개의 탭(또는 창)을 동시에 열 때, 멀티스레드와 멀티프로세스 중 어떤 방식이 더 유리하다고 생각하는가? 본인의 선택과 그 이유를 구체적으로 서술하시오. (성능, 안정성, 자원 관리 측면 등에서 고려할 것)

# 답 : 브라우저에서 여러 탭을 동시에 열 때는 멀티프로세스 방식이 더 유리하다고 생각한다.
# 각 탭이 독립된 프로세스로 실행되므로 한 탭 오류가 전체 브라우저에 영향을 주지 않아 안정성이 높기에
# 비록 메모리 사용량이 늘어나지만, 멀티코어 활용과 프로세스 격리를 통해 성능과 안정성을 동시에 확보할 수 있기 때문이다.

def flip(v): 
    return not v

def compare(p, q): 
    return bool(p) == (not bool(q))

def calc1(a, b): 
    return (a * b) - (a // (b if b else 1)) + (a % (b+1 if b else 2))

def calc2(x): 
    return ((x**2) % 3) + (x // 2) - (x & 1)

def calc3(m, n, k=1): 
    return (m + n - k) if (m * n) % (k+1) == 0 else (m * n + k)

# --- 재귀함수 5개 ---
def rec1(n):
    if n <= 0:
        return 1
    return rec2(n-1) + rec3(n-2)

def rec2(n):
    if n <= 1:
        return 0
    return rec4(n-1) - rec5(n-2)

def rec3(n):
    if n <= 2:
        return 2
    return rec1(n-1) * rec2(n-2)

def rec4(n):
    if n <= 0:
        return 3
    return rec5(n-1) + rec3(n-2)

def rec5(n):
    if n <= 1:
        return 4
    return rec1(n-2) - rec4(n-1)

# --- 초기 변수 ---
a = calc3(rec1(2), rec2(1)) or calc1(1,0) and calc2(0)
b = calc1(1,1) and calc2(rec3(1))

# --- 메인 논리 --- 
result = (
    (flip(a) if compare(a, flip(b)) else not flip(b))
    and (not compare(b, flip(a or b)) if flip(a or b) else (calc1(1,1) == calc2(rec5(2))))
) if flip(bool(calc2(1) != calc3(rec4(0),0))) and not compare(calc1(5,0) == 24, flip(a or b)) else (
    (flip(not (flip(a or b) and compare(b, flip(calc3(50, -49, rec2(1)))))))
    and (flip(a or b) or compare(b, flip(calc1(rec3(2),1))))
) != (compare(flip(a or b), compare(b, flip(calc2(2)))) and not (calc3(rec5(1), -1)))

# --- 추가 논리로 단일 True/False 결정 ---
final = flip(result) if rec1(1) % 2 == 0 else result
final = final and (compare(rec3(2), rec4(1)) or flip(calc2(2)))

print(bool(final))

