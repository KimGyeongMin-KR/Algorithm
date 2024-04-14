N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    s = arr[i]
    for j in range(i):
        if s > arr[j]:
            dp[i] = max(dp[i], dp[j] + s)
        else:
            dp[i] = max(s, dp[i])
print(max(dp))