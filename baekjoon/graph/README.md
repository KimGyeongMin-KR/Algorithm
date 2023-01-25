# [적록색약/G5](https://www.acmicpc.net/problem/10026)
## 설계
1. 전체 순회하며 ["R", "G", "B"] 존재 시, BFS 시작 (일반 버전, 적록색약 버전으로 총 2번)
2. 출발 색상과 다음 색상이 같은 색일 시, "RGB"외 다른 값으로 변경
    - 적록색약 버전일 시, "RG"는 하나로 묶어서 판단
3. 시작 색에서 BFS 종료 시 count에 +1

# [단지번호붙이기/S1](https://www.acmicpc.net/problem/2667)

## 초기 설계

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