from collections import deque
import copy

N = int(input())
graph_nonpenalty = [list(input()) for _ in range(N)]
graph_penalty = copy.deepcopy(graph_nonpenalty)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
queue = deque()
cnt_nonpenalty = 0
cnt_penalty = 0
def bfs(start_color: str, is_penalty: bool):

    graph = graph_penalty if is_penalty else graph_nonpenalty
    
    while queue:
        tr, tc = queue.popleft()
        
        for i in range(4):
            nr, nc = tr + dr[i], tc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == start_color:
                    graph[nr][nc] = "X"
                    queue.append([nr, nc])
                elif is_penalty and start_color in "RG" and graph[nr][nc] in "RG":
                    graph[nr][nc] = "X"
                    queue.append([nr, nc])
    return

for r in range(N):
    for c in range(N):

        t = graph_penalty[r][c]
        if t in ["R", "G", "B"]:
            queue.append([r, c])
            bfs(t, True)
            cnt_penalty += 1
            
        t = graph_nonpenalty[r][c]
        if t in ["R", "G", "B"]:
            queue.append([r, c])
            bfs(t, False)
            cnt_nonpenalty += 1
            

print(cnt_nonpenalty, cnt_penalty)