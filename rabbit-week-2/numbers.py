# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for idx in range(len(absolutes)):
        num = absolutes[idx] if signs[idx] else -absolutes[idx]
        answer += num
    return answer


# 두 정수 사이의 합
def solution(a, b):
    a,b= sorted([a,b])
    return sum(range(a,b+1))


# 나머지가 1이 되는 수 찾기
def solution(n):
    n -= 1
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            n = i
            break
    return n


# 정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(sorted(list(str(n)))[::-1]))


#문자열을 정수로 바꾸기
def solution(s):
    return int(s)