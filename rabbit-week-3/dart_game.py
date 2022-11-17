def solution(s):
    
    answer = []
    num_str = "0123456789"
    op_dict = {
        "S" : lambda x : x,
        "D" : lambda x : x**2,
        "T" : lambda x : x**3,
    }
    
    now_num = 0
    
    for i in s:
        if i in num_str:

            if i == "0" and now_num == 1:
                now_num *= 10
            else:
                answer.append(now_num)
                now_num = int(i)

        elif i in op_dict:
            now_num = op_dict[i](now_num)

        else:
            if i == "*":
                now_num *= 2
                answer[-1] *= 2
            else:
                now_num *= -1
                
    answer.append(now_num)
    
    return sum(answer)