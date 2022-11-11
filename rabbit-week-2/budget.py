def solution(d, budget):
    answer = 0
    for m in sorted(d):
        budget -= m
        if budget < 0:
            break
        answer += 1
    return answer