N = int(input())
cnt = 0
total = 0
while total <= N:
    cnt += 1
    total += cnt
print(cnt - 1)