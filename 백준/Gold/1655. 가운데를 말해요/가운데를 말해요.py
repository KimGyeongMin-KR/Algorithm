import heapq as hq
import sys

input = sys.stdin.readline

left_max_heap = []
right_min_heap = []

N = int(input())
arr = [int(input()) for _ in range(N)]
mid = 10**6 + 1
answer = []

for x in arr:

    if x < mid:
        hq.heappush(left_max_heap, -x)
        
        if len(left_max_heap) > len(right_min_heap) + 1:
            pd = hq.heappop(left_max_heap)
            hq.heappush(right_min_heap, -pd)
    else:
        hq.heappush(right_min_heap, x)
        
        if len(right_min_heap) > len(left_max_heap):
            pd = hq.heappop(right_min_heap)
            hq.heappush(left_max_heap, -pd)
            
    mid = -left_max_heap[0]
    answer.append(str(mid))
    
print("\n".join(answer))