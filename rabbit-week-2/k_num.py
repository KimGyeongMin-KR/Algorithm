def solution(array, commands):
    
    # answer = []
    # for c in commands:
    #     start, end, idx = c[0], c[1], c[2]
    #     answer.append(sorted(array[start-1 : end])[idx-1])
    
    answer = [ sorted(array[x[0]-1 : x[1] ])[ x[2]-1 ] for x in commands ]

    return answer