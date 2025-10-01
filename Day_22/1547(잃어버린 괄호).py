# https://www.acmicpc.net/problem/1541

parts = input().replace('+', ' ').split('-') # - 기준으로 분할하기

total = sum(map(int, parts[0].split())) # - 앞의 모든 수는 다 더하기

for part in parts[1:]: 
    total -= sum(map(int, part.split())) # 음수 ~ 음수 앞 수 까지 다 더한 수를 빼기

print(total)
