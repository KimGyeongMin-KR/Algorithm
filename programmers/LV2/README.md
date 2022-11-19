# 프로그래머스 Lv.2 알고리즘 문제 생각 노트 

( JandenCase)


# [JadenCase](https://school.programmers.co.kr/learn/courses/30/lessons/)
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