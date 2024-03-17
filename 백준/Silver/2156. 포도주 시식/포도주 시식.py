import sys
input = sys.stdin.readline

N = int(input())
input_list = [0] * 3 + [int(input()) for _ in range(N)]
dp = [0] * 3 + [0] * N

def solution():
    for i in range(3, N + 3):
        dp[i] = max(
            input_list[i] + input_list[i - 1] + dp[i - 3],
            input_list[i] + dp[i - 2],
            dp[i - 1],
        )
    return max(dp[3:])
print(solution())