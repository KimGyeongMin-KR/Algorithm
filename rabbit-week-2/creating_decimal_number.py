from itertools import combinations

def solution(nums):

    sum_list = list(map(lambda x: sum(x), list(combinations(nums, 3))))
    cnt = 0
    
    for i in list(sum_list):
        for d in range(2,int(i**0.5) + 1):
            if i % d == 0:
                break
        else:
            cnt += 1

    return cnt

# combinations 쓰지 않고 만들어 보기