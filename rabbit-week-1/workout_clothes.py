def solution(n, lost, reserve):

    intersection = set(lost) & set(reserve)

    lost = sorted(set(lost) - intersection)
    reserve = sorted(set(reserve) - intersection)

    n -= len(lost)

    for idx in reserve:

        if idx-1 in lost:
            lost.pop(lost.index(idx-1))
            n+=1

        elif idx+1 in lost:
            lost.pop(lost.index(idx+1))
            n+=1
            
    return n