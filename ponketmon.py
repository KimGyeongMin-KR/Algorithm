def solution(nums):
    answer = len(nums)//2
    ps= len(set(nums))
    return answer if answer<= ps else ps