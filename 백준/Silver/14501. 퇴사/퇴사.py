N = int(input())
tt = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for idx in range(N-1, -1, -1):
    due, money = tt[idx]
    if due + idx > N:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + 1], money + dp[due + idx])
print(max(dp))