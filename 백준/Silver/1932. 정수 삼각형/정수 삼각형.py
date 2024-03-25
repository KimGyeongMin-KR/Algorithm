N = int(input())
p = [[0]] + [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N + 1):
    for j in range(i):
        if j == 0:
            p[i][j] = p[i-1][0] + p[i][j]
        elif j == i - 1:
            p[i][j] = p[i-1][-1] + p[i][j]
        else:
            p[i][j] = max(
                p[i-1][j-1],
                p[i-1][j],
            ) + p[i][j]
print(max(p[-1]))