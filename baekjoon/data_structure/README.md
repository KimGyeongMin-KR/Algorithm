# [가운데를 말해요/G2](https://www.acmicpc.net/problem/1655)
- 최대 힙, 중앙 값(최소 힙의 첫번째 값), 최소 힙
- 중앙 값 보다 큼 -> 최소 힙(오른쪽), 작음 -> 최대힙(왼쪽)
- 왼쪽 힙 길이는 오른쪽 힙 길와 같거나 1 커야함 (불 충족 시 서로 옮김, 왼쪽 힙 첫번째가 중앙값이므로)

# [이중 우선순위 큐/G4](https://www.acmicpc.net/problem/7662)
- 최소 힙과 최대 힙과 삭제 여부 싱크를 맞춰줄 리스트
- 힙에서 제거 시 삭제 안 됐을 때까지 pop
- 삭제 안된 최소 최대 출력


# [전력망](https://www.acmicpc.net/problem/1620)

## 설계
- 하나의 딕셔너리에 이름: 숫자, 숫자: 이름 을 같이 넣는다.
- 따로 나눌까 하다가 하나로 합쳐도 겹치지 않기때문에 하나로 진행

<details>
<summary>나의 정답</summary>

```python
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

total_dict = {}

for i in range(1, m+1):
    pm = input().strip().replace("\n", "")
    total_dict[pm] = i
    total_dict[i] = pm

for _ in range(n):
    q = input().strip().replace("\n", "")
    try:
        q = int(q)
    except ValueError:
        pass
    # if q.isdigit():
    #    q = int(q)

    print(total_dict[q])
```
</details>

- readline() 시 '\n'도 같이 받아오기에 변환해 주어야했다.
- try except 말고 isdigit() 메서드를 사용해도 된다.
