def solution(s):
    answer = ' '
    for i in s:
        if answer[-1] == ' ' and i != ' ':
            answer += i.upper()
        else:
            answer += i.lower()
    return answer[1:]