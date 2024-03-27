N = int(input())
ba = list(map(int, input().split()))
dp1 = [1] * N
dp2 = [1] * N
for i in range(N):
    for j in range(i):
        ri = -(i + 1)
        rj = -(j + 1)
        if ba[i] > ba[j]:
            dp1[i] = max(dp1[j] + 1, dp1[i])
        if ba[ri] > ba[rj]:
            dp2[ri] = max(dp2[rj] + 1, dp2[ri])
print(max([i + j for i, j in zip(dp1, dp2)]) - 1)
