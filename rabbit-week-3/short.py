# 가운데 글자 가져오기
def solution(s):
    c = len(s)//2
    return s[c] if len(s)%2 else s[c-1:c+1]


# 수박수박수?
def solution(n):
    answer = ''
    cnt = 0
    while cnt < n:
        answer += '수박'[cnt%2]
        cnt += 1
    return answer


# 제일 작은 수 제거
def solution(arr):
    del arr[arr.index(min(arr))]
    return arr if arr != [] else [-1]


# 핸드폰 번호 가리기
def solution(phone_number):
    return f"{len(phone_number[:-4])*'*'}{phone_number[-4:]}"


# 문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False