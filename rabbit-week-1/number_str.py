# 없는 숫자 더하기
def solution(numbers):
    std = {i for i in range(10)}
    answer = sum(std-set(numbers))
    return answer

# 자릿수 더하기
def solution(n):
    answer = sum(map(int, list(str(n))))
    return answer

# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = list(map(int, list(str(n))[::-1]))
    return answer

# 짝수와 홀수
def solution(num):
    answer = 'Odd' if num%2 else 'Even'
    return answer
    
# 평균
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer