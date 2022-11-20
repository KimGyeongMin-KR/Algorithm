def solution(n, arr1, arr2):
    answer = []

    for idx in range(n):

        map_row = ''
        bin_str_row = format(arr1[idx]|arr2[idx], 'b').zfill(n)
        
        for item in bin_str_row:
            if item == '1':
                map_row += '#'
            else:
                map_row += ' '

        answer.append(map_row)
        
    return answer


import re
def solution(n, arr1, arr2):
    map_ = [bin(x | y)[2:].zfill(n) for x, y in zip(arr1, arr2)]
    answer = []
    for i in map_ :
        tmp = re.sub('1', '#', i)
        tmp = re.sub('0', ' ', tmp)
        answer.append(tmp)
    return answer