import sys
import heapq as hq

input = sys.stdin.readline

queue = []
num_dict = {}

for _ in range(int(input())):
    bf_num = int(input())
    is_minus = bf_num < 0
    abs_num = abs(bf_num)
    
    if abs_num:
        hq.heappush(queue, abs_num)
        
        if not num_dict.get(abs_num, ''):
            num_dict[abs_num] = [0, 0]

        if is_minus:
            num_dict[abs_num][0] += 1
        else:
            num_dict[abs_num][1] += 1
    else:
        if not queue:
            print(0)
            continue
            
        answer = hq.heappop(queue)
        
        if num_dict[answer][0]:
            num_dict[answer][0] -= 1
            print(-answer)
        else:
            num_dict[answer][1] -= 1
            print(answer)