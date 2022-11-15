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
# sum()함수 있을 때 O(N^2)
# sorted() O(NlogN)
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