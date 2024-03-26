L1, L2 = input(), input()
l1, l2 = len(L1), len(L2)
dp = [[0] * (l2+1) for _ in range(l1)]

for i in range(l1):
    for j in range(1, l2+1):
        same = L1[i] == L2[j-1]
        dp[i][j] = max(
            dp[i-1][j],
            dp[i][j-1],
            dp[i-1][j-1] + same,
        )
print(dp[-1][-1])