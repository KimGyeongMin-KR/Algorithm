T = int(input())
def solution():
    N = int(input())
    dp = [[0, 0] + list(map(int, input().split())) for _ in range(2)]
    for i in range(2, N+2):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + dp[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + dp[1][i]
    return max(dp[0][N+1], dp[1][N+1])

for _ in range(T):
    print(solution())