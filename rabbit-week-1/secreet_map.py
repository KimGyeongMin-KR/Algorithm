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