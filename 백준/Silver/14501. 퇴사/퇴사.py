N = int(input())
dp = [0 for _ in range(N)]
time_table = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    d, m = time_table[i]
    if d + i >= N + 1:
        continue
    dp[i] = max(dp[i], m)
    for j in range(i):
        due, _ = time_table[j]
        if  due + j >= i + 1:
            continue
        dp[i] = max(dp[i], dp[j] + m)
print(max(dp))