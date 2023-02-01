# [적록색약/G5](https://www.acmicpc.net/problem/10026)
## 설계
1. 전체 순회하며 ["R", "G", "B"] 존재 시, BFS 시작 (일반 버전, 적록색약 버전으로 총 2번)
2. 출발 색상과 다음 색상이 같은 색일 시, "RGB"외 다른 값으로 변경
    - 적록색약 버전일 시, "RG"는 하나로 묶어서 판단
3. 시작 색에서 BFS 종료 시 count에 +1


# [토마토/G5](https://www.acmicpc.net/problem/7576)
## 설계
1. 1의 좌표를 queue에 담는다.
2. queue를 기반으로 BFS 시작
    - 동 서 남 북 조회하여 0일 경우 (현위치 값 + 1)을 대입
3. 배열의 가장 큰 값 - 1 을 출력

## 초기 설계 (시간 초과)
- 전체를 순회하며 1이 나올 시 해당 좌표를 기준으로 BFS 시작
- 동 서 남 북 조회하여, (현위치 값 + 1)이 해당 값보다 작다면 대입, 0일 경우 바로 대입



# [숨바꼭질/S1](https://www.acmicpc.net/problem/1697)

- [ ] 복습
## 설계
- [숫자, 횟수]를 담는 큐
- 큰 숫자에서 떨구는 구조, BFS
- 방문하지 않은 것들만 append

# [단지번호붙이기/S1](https://www.acmicpc.net/problem/2667)

## 설계

1. 전체를 순회
    - 1의 값이 나온다면, queue 인덱스 삽입, 자신 0으로 치환, dfs시작
2. dfs
    - 아파트 개수는 1부터 시작
    - 동서남북 조회
        - 조건문 row 좌표, col 좌표 각각 0이상 N미만
        - 1의 값이 나온다면 아파트 개수 +1, 자신 0 치환
        - queue에 현재 인덱스(다음) 삽입
    - 끝난다면 아파트 개수 삽입
3. 출력

> 1번의 하위 항목이 2번의 조건문 아래로 겹치는 것(반복 코드)은 구현 할 때, 값이 1이 아니라면 continue로 바꿔서 코드를 조금 더 깔끔하게 바꿨음.

<details>
<summary>코드</summary>

```python
from collections import deque

queue = deque()
N = int(input())
next_rows = [0, 0, 1, -1]
next_cols = [1, -1, 0, -0]
apts = [list(map(int, input())) for _ in range(N)]
results = []


for row in range(N):
    for col in range(N):
        if apts[row][col] != 1:
            continue

        apts[row][col] = 0
        queue.append([row, col])
        count = 1

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + next_rows[i], c + next_cols[i]
                if 0 <= nr < N and 0 <= nc < N and apts[nr][nc] == 1:
                    count += 1
                    apts[nr][nc] = 0
                    queue.append([nr, nc])

        results.append(count)

print(len(results))
print('\n'.join(map(str, sorted(results))))
```
</details>


# [연결 요의 개수/S2](https://www.acmicpc.net/problem/11724)
- 복습 필요(재귀적)
## 설계
v1
1. 전체 순회하면서 노드겸 인덱스가 방문 내역에 없다면 dfs 시작과 count += 1
2. 방문하는 곳 추가와 인접 노드를 덱에 넣고 비어있을 때까지 반복
    - 조건은 방문했던 곳에 없어야한다.
    
v2
1. 전체 순회하면서 노드겸 인덱스가 방문 내역에 없다면 dfs 시작과 count += 1
2. 방문하는 곳 리스트 체크 후 인접 노드를 순회하며 dfs재귀 호출
    - 조건은 방문하지 않았던 곳이어야한다.

<details>
<summary>코드</summary>

```python
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

m, n = map(int, input().split())
graph = {x : set() for x in range(1, m+1)}
v = [False] * (m+1)

for _ in range(n):
    n1, n2 = map(int, input().split())
    graph[n1].add(n2)
    graph[n2].add(n1)
    
    
def dfs(num):
    v[num] = True
    
    for node in graph[num]:
        if not v[node]:
            dfs(node)

cnt = 0

for x in range(1, m+1):
    if not v[x]:
        cnt += 1
        dfs(x)

print(cnt)
```
</details>



# [1만들기 /S3](https://www.acmicpc.net/problem/1463)

<details>
<summary>나의 정답</summary>
</details>