# [이중 우선순위 큐](https://www.acmicpc.net/problem/7662)



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
