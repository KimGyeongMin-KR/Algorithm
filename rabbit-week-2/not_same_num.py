def solution(arr):
    # answer = []
    # for i in arr:
        # if len(answer) == 0 or answer[-1] != i:
            # answer.append(i)
    answer = [arr[x] for x in range(len(arr)) if x == 0 or arr[x] != arr[x-1] ]
    return answer