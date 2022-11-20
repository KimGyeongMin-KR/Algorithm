def solution(N, stages):

    stage = [0] * (N+2)
    fail_per = [0] * (N+2)

    for st in stages:
        stage[st] += 1
    
    for st in range(len(stage)):
        clear_people = sum(stage[st:]) if sum(stage[st:]) != 0 else 1 # 나눠줄 분모
        fail_per[st] = (stage[st]/clear_people, st)
        
    failer_sorted = sorted(fail_per[1:-1], key = lambda x : (-x[0], x[1]))
    answer = [ x[1] for x in failer_sorted ]
    
    return answer

# 개선 코드
def solution(N, stages):

    stage = [0] * (N+2)
    fail_per = [0] * (N+2)
    reached = len(stages)

    for st in stages:
        stage[st] += 1
    
    for st in range(1,len(stage)):
        reached -= stage[st-1]
        fail_per[st] = (stage[st]/reached, st) if stage[st] else (0,st)
        
    failer_sorted = sorted(fail_per[1:-1], key = lambda x : (-x[0], x[1]))
    answer = [ x[1] for x in failer_sorted ]
    
    return answer



# 참고하면 좋을 코드
from collections import Counter

def solution(N, stages):
    stage = Counter(stages)
    total = [len([x for x in stages if x >= i+1]) for i in range(N)]
    result = [(stage[x+1] / total[x] if total[x] != 0 else 0, x+1) for x in range(N)]
    result.sort(reverse = True, key = lambda x : x[0])
    return [x[1] for x in result]