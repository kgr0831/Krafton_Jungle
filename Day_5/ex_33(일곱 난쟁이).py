inputDatas = []

for _ in range(9) :
    inputDatas.append(int(input()))

total = sum(inputDatas)-100

def findfake():
    for k in inputDatas:
        for i in inputDatas:
            if k == i:
                continue
            if k + i == total:
                return k, i

a,b = findfake()

inputDatas.remove(a)
inputDatas.remove(b)

print(*sorted(inputDatas), end = "\n")