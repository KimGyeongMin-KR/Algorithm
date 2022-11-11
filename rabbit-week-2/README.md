# 프로그래머스 알고리즘 문제 생각 노트 ft. 토끼반_2주차_Lv.1

(실패율, 소수 만들기, K번째수, 예산, 같은 숫자는 싫어, 음양 더하기, 두 정수 사이의 합, 나머지가 1이 되는 수 찾기, 정수 내림차순으로 배치하기, 문자열을 정수로 바꾸기 )


# [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/failure_rate.py)

***실패율 정의에 주목하였음***

실패율은 다음과 같이 정의한다.
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
## 초기 설계

1. 각 스테이지에 몇 명이 있는지 확인 (스테이지 == 인덱스)
2. (각 스테이지 실패율, 인덱스) 배열을 만듦
3. 실패율은 내림차순, 인덱스는 오름차순 정렬
4. 인덱스만 뽑아서 반환


# [소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/creating_decimal_number.py)
1. nC3 조합들 각각 합을 배열에 담는다.
2. 배열에서 각 수를 제곱근까지의 수로 소수를 판별 후 개수 반환

# [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/k_num.py)
- 슬라이싱 후 해당 인덱스의 값을 담은 배열을 반환


# [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/budget.py)
- 정렬된 신청금 배열을 돌며 예산이 음수가 되기 전까지 빼다가 횟수 반환


# [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/not_same_num.py)
- 이전의 숫자와 다르다면 배열에 담아서 반환

---------------------
# numbers.py 모음
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-2/numbers.py)
# [음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501)
- T F에 따라 + - 적용

# [두 정수 사이의 합](https://school.programmers.co.kr/learn/courses/30/lessons/12912)
- sum(range())를 사용하여 사이값 더하기

# [나머지가 1이 되는 수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/87389)
- 제곱근까지 약수의 최솟값을 반환, 없을 경우 소수(자신)을 반환

# [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)
- 문자열 -> 리스트 -> 내림차순 정렬 -> 연결 -> 형변환

# [문자열을 정수로 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/12925)
- int()