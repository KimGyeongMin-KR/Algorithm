# 프로그래머스 알고리즘 문제 생각 노트 ft. 토끼반_3주차_Lv.1 & 2

( 다트 게임, H-Index, 폰켓몬, 올바른 괄호, 콜라츠 추측,  수박수.., 가운데 글자 가져오기, 제일 작은 수 제거, 핸드폰 번호 가리기, 문자열 내 p와 y의 개수)


# [다트게임](https://school.programmers.co.kr/learn/courses/30/lessons/42889)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/dart_game.py)
## 설계
- 주어진 문자열을 돌면서 숫자, 옵션, 보너스를 구분 지음
    - 숫자 중 10이 들어올 수 있어 "0"을 기준으로 이전 숫자가 1임을 판단 후 * 10
- 옵션과 보너스는 조건대로 연산하면 됨
    - 옵션 중 현재 값과 이전 값에 대한 계산이 필요하므로 점수를 배열에 저장하고 [-1] 활용


# [H-index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/H-Index.py)
## 설계

0. 주어지는 리스트(논문_리스트) 오름차순 정렬
1. 논문_리스트에서 인용한 횟수 최댓값까지 순회, 값은 (h)
2. 현재 기준 인덱스의 값은(논문_리스트[논문_idx]) h 이상이어야 하며, 길이도 h 이상이어야 한다.
    - 기준 값이 h보다 작다면 기준 인덱스 +1
    - 길이가 h보다 작다면 중지
3. 최댓값 갱신

<img src="/images/H-index.jpeg" width="600" />

## 정답 코드에서 반례 발견
- 설계 2-1에서 인덱스를 +1 해줬을 경우 같은 숫자가 나올 수 있음을 발견

## 해결
- 2-1에서 h이상이 되는 수를 찾기까지 인덱스를 더해줌

## 간단한 답
- 최대를 찾는 것이기에, 배열의 길이로부터(역순) 순회 : h
- h보다 큰 값을 세주고(count), count가 h보다 크면 return

# [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/ponketmon.py)
- 안 겹치는 폰켓몬과 전체 포켓몬을 2로 나눈 몫 중 작은 것이 답.


# [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/right_bracket.py)
- 기준 = 0, '('이 들어오면 +1, 반대는 -1
- 기준이 한 순간도 음수가 되면 안됨, 결과 값은 0이어야함


# [콜라츠 추측](https://school.programmers.co.kr/learn/courses/30/lessons/12943)
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/not_same_num.py)
- 홀짝 판단 후 계산, 계산 횟수 체크 

---------------------
# numbers.py 모음
- [나의 답안](https://github.com/KimGyeongMin-KR/algoritm/blob/main/rabbit-week-3/short.py)
# [수박수박수박수박수박수?](https://school.programmers.co.kr/learn/courses/30/lessons/12922)
- 나머지 '%' 활용

# [가운데 글자 가져오기](https://school.programmers.co.kr/learn/courses/30/lessons/12903)
- //2 혹은 //2 -1 : //2 + 1

# [제일 작은 수 제거](https://school.programmers.co.kr/learn/courses/30/lessons/12935)
- del과 젤 작 숫자의 인덱스로 해결

# [핸드폰 번호 가리기](https://school.programmers.co.kr/learn/courses/30/lessons/12948)
- 인덱싱 문제

# [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)
- lower(), count()로 해결