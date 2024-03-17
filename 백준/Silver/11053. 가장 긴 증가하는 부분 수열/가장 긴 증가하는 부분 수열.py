N = int(input())
input_list = list(map(int, input().split()))
dp = [1] * N
def solution():
    for i in range(N):
        for j in range(i):
            if input_list[j] < input_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(solution())