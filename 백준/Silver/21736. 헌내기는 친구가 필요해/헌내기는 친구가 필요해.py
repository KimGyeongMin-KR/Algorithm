from collections import deque


def bfs(campus, sx, sy):
    visited = [[0] * M for _ in range(N)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] == 'O':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif campus[nx][ny] == 'P':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    if cnt == 0:
        return 'TT'
    else:
        return cnt

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if campus[x][y] == 'I':
            print(bfs(campus, x, y))
            exit()