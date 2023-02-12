
li = [0, 1, 3] + [0] * 1000
n = int(input())

for idx in range(3, 1001):
    ap = -1 if idx % 2 else 1
    li[idx] = li[idx-1] * 2 + ap
print(li[n] % 10007)