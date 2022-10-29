# 프로그래머스 알고리즘 문제 생각 노트 ft. 토끼반_1주차_Lv.1

( 비밀지도, 완주하지 못한 선수, 체육복, 약수의 개수와 덧셈, 숫자 문자열과 영단어, 없는 숫자 더하기, 자릿수 더하기, 자연수 뒤집어 배열로 만들기, 짝수와 홀수, 평균 구하기 )


# [비밀 지도](https://school.programmers.co.kr/learn/courses/30/lessons/17681#)

## 초기 설계

1. 각 정수의 숫자들을 2진수 비트열로 바꿔준다 -> [2진수로 변환하기](https://brownbears.tistory.com/467)

2. 두 개의 배열에서 인덱스가 맞는 것끼리 비트연산 해준다(하나라도 1이면 1) -> [비트연산](https://wikidocs.net/1161)

3. 빈문자열에 1이면 # 0이면 공백을 채워준다.

## 변화된 설계
- 비트연산을 찾는 도중 두 정수를 넣으면 알아서 비트연산이 되는 것을 찾아서 변경
1. 두 개의 배열에서 인덱스가 맞는 것끼리 비트연산을 해준다.(or연산 : a`|`b )
2. 각 정수의 숫자들을 2진수 비트열로 바꿔준다.(format(숫자, 타입))
3. 빈 문자열에 1이면 # 0이면 공백을 채워준다.

## 에러

1. 1번의 비트연산 후 2진수로 바꿔줄 때 앞 자리가 0일 경우 자리수가 줄어듦
    - `zfill(원하는 자리수)`를 통해서 해결


# [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

## 초기 설계

1. 완주하지 못한 사람은 1명이기 때문에 집합으로 빼서 한명이 나온다면 정답
2. 그렇다면 동명이인이 있어서 집합으로 뺐을 때 None값이 나온다면?
3. set으로 정답을 돌면서 각각 count를 써서 개수가 다르면 정답
## 에러

1. count()함수는 O(n)의 시간이 걸린다.
2. 최악의 상황 10만명 중 동명이인이 2명이고 완주자에서 마지막에 배치되어 모두 돌아야할 경우 - 약 100억 번의 연산 필요 예상 $\frac{n(n+1)}{2}*2$ >>>> O($n^2$)


## 변화된 설계

1. 초기 설계와 같이 먼저 집합으로 빼주고 값이 있다면 정답을 출력
2. 동명이인이 있는 경우.
    1. 참여자 배열을 돌면서 {'이름' : 사람수}를 구해준다.
    2. 완주자 배열을 돌면서 딕셔너리['이름'] -= 1 을 해주고 값이 0이면 삭제한다.
    3. 키 값들의 첫 번째 데이터를 뽑는다


# [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)

## 초기 설계

1. 도난 배열과 여벌이 배열의 교집합을 각각 빼준다.
2. 전체 수에서 갱신된 도난 배열의 길이를 빼주고 시작한다.
3. 갱신된 여벌 배열의 각각의 값에서 -1 또는 +1 의 값이 갱신 도난 배열에 있는지 확인
    - 있다면 정답 +1, 갱신 도난 배열에서 제외


# [약수의 개수와 덧셈](https://school.programmers.co.kr/learn/courses/30/lessons/77884)

## 초기 설계
- 약수의 개수가 홀수인 경우를 좀 생각해 보니 어떤 수의 제곱인 경우 홀수가 됨
- 제곱근이 정수 값과 같은지 판단하면 끝


# [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301)

## 초기 설계

1. 영단어에 해당하는 "숫자"를 딕셔너리로 만든다
2. [replace()](https://ooyoung.tistory.com/77)로 바꿔준다. (에러 사항 - int로 변환해 주어야함)

---------------------
# number_str.py 모음
# [없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051)
- 0~9까지의 집합에서 주어진 숫자배열과 차집합의 합

# [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/12931)
- 분리하여 map()활용 int변환 후 더하기

# [자연수 뒤집어 배열로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12932)
- 자릿수 더하기와 비슷함(분리, map)

# [짝수와 홀수](https://school.programmers.co.kr/learn/courses/30/lessons/12937)
- %2 나머지로 판별

# [평균](https://school.programmers.co.kr/learn/courses/30/lessons/12944)
- 평균