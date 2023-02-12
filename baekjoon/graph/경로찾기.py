from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

graph_map = [list(map(int, input().split())) for _ in range(n)]
graph_dict = {i: [] for i in range(n)}
graph = [[0] * n for _ in range(n)]

for ridx, row in enumerate(graph_map):
    for cidx, col in enumerate(row):
        if col:
            graph_dict[ridx].append(cidx)

def bfs(start):
    visited = []
    queue = deque(graph_dict[start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            graph[start][node] = 1
            queue.extend(graph_dict[node])
            
for i in range(n):
    bfs(i)

for x in graph:
    print(*x)
    