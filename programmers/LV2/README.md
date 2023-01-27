# 프로그래머스 Lv.2 알고리즘 문제 생각 노트 

( 숫자의 표현, JandenCase, 이진 변환 반복하기, 최솟값 만들기)


# [전력망](https://school.programmers.co.kr/learn/courses/30/lessons/86971)

## 설계
- 딕셔너리, 리스트 형태의 그래프를 생성
- 간선을 하나씩 제거하고 해당 노드를 골라서 bfs로 길이 반환 후 간선 복구
- 차이를 구하고 필요 시(더 낮을 때) 갱신

<details>
<summary>나의 정답</summary>

```python
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
```
</details>

- zip(내림차순배열, 오름차순배열)


# [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)
- 복습 필요
## 설계
- 방문할 수 있는 모든 곳을 탐색
    - 남은 피로도를 기준으로 판단
- 가장 큰 던전을 입장한 횟수 반환

<details>
<summary>정답 코드</summary>

```python
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


```
</details>


# [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924)
- 문제 : 숫자 n이 주어졌을 때, 연속된 자연수의 합으로 n을 만들 수 있는 경우의 수
- 제한 : n은 10000이하 자연수
<details>
<summary>나의 정답</summary>

```python
def solution(n):
    r = 0
    for i in range(n, 0, -1):
        cnt = i
        for j in range(i-1, -1, -1):
            if cnt == n:
                r+=1
                break
            elif cnt > n:
                break
            cnt += j
    return r

# 참고하면 좋을 훨씬 좋은 코드
# https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/
def solution(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
```
</details>

# [JadenCase](https://school.programmers.co.kr/learn/courses/30/lessons/12951)
<details>
<summary>나의 정답</summary>

```python
def solution(s):
    answer = ' '
    for i in s:
        if answer[-1] == ' ' and i != ' ':
            answer += i.upper()
        else:
            answer += i.lower()
    return answer[1:]
```
</details>

## 초반 설계
- split을 통해 나눠주고 lower과 upper변형 후 join으로 간단하게 해결
## 애로 사항
- 여러개의 공백이 들어와도 띄어 쓰기를 하나로 만들어주면 될거라는 혼자만의 쉐도우 복싱
## 바뀐 설계
- 최근 들어간 문자가 ' '이고 현재 문자가 ' '이 아니라면 upper 후 삽입
- 나머지는 lower후 삽입


# [이진 변환 반복하기](https://school.programmers.co.kr/learn/courses/30/lessons/70129)
<details>
<summary>나의 정답</summary>

```python
def solution(s):
    count = 0
    zero_count = 0
    while s != "1":
        # 0개수와 1개수
        one_num = s.count('1')
        zero_num = len(s) - one_num
        # s 갱신
        s = format(one_num, 'b')
        # count +
        count += 1
        zero_count += zero_num

    return [count, zero_count]
```
</details>

- format(정수, 형식) ; 'b' binary ex) format(4, 'b') >>> "100"


# [최솟값 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12941)
<details>
<summary>나의 정답</summary>

```python
def solution(A,B):
    return sum([a*b for a,b in zip( sorted(A), sorted(B, reverse = True))])
```
</details>

- zip(내림차순배열, 오름차순배열)