# [PPAP/G4](https://www.acmicpc.net/problem/16120)

## 설계
- P일 때는 p count +1, AP 일 때는 -1
    - p count는 0 이하가 되면 중지
    - 첫글자는 무조건 P (P만 있는 경우 PPAP)
    - P거나 AP가 아니라면 NP (ex. AA)
    - p count 는 끝났을 때 무조건 1이어야 정답


# [회의실 배정](https://www.acmicpc.net/problem/1931)

- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/baekjoon/greedy/S1-1931.py)


## 초기 생각
- 10만개이기 때문에 O($n^2$)은 나와서는 안 될 것
- 최대한 많이 겹치는 것을 먼저 빼줘야하나?
    - 몇번 겹치는지를 확인하는 것부터 시간 초과가 날 것이다.
- 제일 먼저 튜플을 사전 순으로 정렬해 주어야 할 것.
- 사전 순이기 때문에 시작 n번째 인덱스 다음 n+1번째의 시작 시간은 같거나 클 것
    - 같다면 끝 시간은 무조건 클 것이기 때문에 pass
    - 다르다면 n의 끝 시간과 n+1의 끝 시간을 비교하여 더 작은 것이 기준
        - n과 회의 시간이 겹친다면 pass
- 시작 시간과 끝 시간이 같을 경우를 고민해야 됨
    - 기준이 되고 회수도 +1

## 고민 후 설계
1. (코드 이해의 핵심) 주어진 회의 시간을 튜플로 받고 오름차순으로 정렬
2. 첫 번째 인자로 기준 시작
3. 다음 회의가 기준 회의보다 빨리 끝나나?
    - 그렇다면 기준은 다음 회의
4. 다음 회의의 시작이 기준 회의와 안 겹치나 (다음 회의 시작 >= 기준 회의 끝)
    - 그렇다면 기준은 다음 회의, 회의의 개수 + 1

## 에러
1. 초반 생각에 회의를 어떻게 지워나가야 하는 것에 시간을 투자함
2. 회의가 시작하마자 끝나는 경우를 따로 나눠보려고 하여 오히려 생각이나 로직이 꼬임


# [보물](https://www.acmicpc.net/problem/1026)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/baekjoon/greedy/S4-1026.py)

## 초기 설계
- 문제에서는 두 번째 배열의 재배열을 금지하였지만 최솟값을 출력하는 것이기에 상관 없다.


# [거스름돈](https://www.acmicpc.net/problem/5585)


<details>
<summary>답</summary>

```python
n = 1000 - int(input())
cnt = 0
for x in [500, 100, 50, 10, 5, 1]:
    cnt += n // x
    n = n % x
print(cnt)
```
</details>



# [수들의 합/S5](https://www.acmicpc.net/problem/)

## 설계
- 1부터 차례대로 더해주고 주어진 값보다 커지는 순간 더한 횟수 -1 출력


# [수들의 합](https://www.acmicpc.net/problem/1439)
- 이전과 다른 숫자일 때 +1

<details>
<summary>답</summary>

```python
str_num = input()
idx_cnt = [0, 0, 1000000]
prev = 3
for num in str_num:
    num = int(num)
    if prev != num:
        idx_cnt[num] += 1
        prev = num
print(min(idx_cnt))
```
</details>