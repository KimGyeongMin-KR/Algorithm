N = int(input())
input_list = [0] + list(map(int, input().split()))
dp = [-1] + [0] * N

def solution():
    for i in range(1, N+1):
        dp[i] = max(input_list[i], input_list[i] + dp[i - 1])
    return max(dp[1:])

print(solution())
