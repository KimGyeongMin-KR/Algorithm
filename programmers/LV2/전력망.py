from collections import deque
graph = {}

def bfs(t):
    queue = deque([t])
    v = set()
    while queue:
        node = queue.popleft()
        if node not in v:
            v.add(node)
            queue += deque(graph[node])
    return len(v)

def solution(n, wires):
    global graph

    answer = n
    graph = {x: set() for x in range(1, n+1)}

    for i,j in wires:
        graph[i].add(j)
        graph[j].add(i)
        
    for i, j in wires:
        graph[i] -= {j}
        cnt = abs(n - 2*bfs(i))
        graph[i].add(j)

        if cnt < answer:
            answer = cnt
    return answer