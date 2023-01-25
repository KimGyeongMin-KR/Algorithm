from collections import deque
import sys

input = sys.stdin.readline
c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
queue = deque()
dc = [0, 0, 1, -1]
dr = [1, -1, 0, 0]


for y in range(r):
    for x in range(c):
        if graph[y][x] == 1:
            queue.append([y, x])

def bfs():
    while queue:
        tc, tr = queue.popleft()
        
        for i in range(4):
            nc, nr = tc + dc[i], tr + dr[i]
            if 0 <= nc < r and 0 <= nr < c and graph[nc][nr] == 0:
                graph[nc][nr] = graph[tc][tr] + 1
                queue.append([nc, nr])


bfs()
                
days = set(sum(graph, []))

if 0 in days:
    print(-1)
else:
    print(max(days) - 1)
