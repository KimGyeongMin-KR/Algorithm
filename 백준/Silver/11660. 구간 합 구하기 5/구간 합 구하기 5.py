import sys
input=sys.stdin.readline
def solution():
    N, M = list(map(int, input().split()))
    a2d = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N+ 1):
        for j in range(1, N+ 1):
            a2d[i][j] = a2d[i][j] + a2d[i][j-1] + a2d[i-1][j] - a2d[i-1][j-1]
    for _ in range(M):
        x1, y1, x2, y2 = list(map(int, input().split()))
        print(
            a2d[x2][y2]
            - a2d[x1-1][y2]
            - a2d[x2][y1 - 1]
            + a2d[x1-1][y1-1]
        )
solution()