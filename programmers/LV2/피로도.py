from collections import deque
answer = 0
N = 0
v = []

def dfs(k, d,  cnt):
    global answer
    if cnt > answer:
        answer = cnt
        
    for i in range(N):
        if k >= d[i][0]:
            dfs(k - d[i][1], d[:i] + d[i+1:], cnt + 1)


def solution(k, dungeons):
    global v, N
    N = len(dungeons)
    v = [0] * N
    dfs(k, dungeons, 0)
    
    return answer


# 다른 답
answer = 0
N = 0
v = []

def dfs(k, d,  cnt):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(N):

        if not v[i] and k >= d[i][0]:
            v[i] = 1
            dfs(k - d[i][1], d, cnt + 1)
            v[i] = 0


def solution(k, dungeons):
    global v, answer, N
    answer = 0
    N = len(dungeons)
    v = [0] * N
    dfs(k, dungeons, 0)

    return answer