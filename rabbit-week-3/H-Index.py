def solution(m):
    answer = 0
    m_idx = 0
    m.sort()
    for i in range(max(m)+1):
        
        if m[m_idx] < i:
            m_idx += 1
            
        if len(m[m_idx:]) >= i:
            answer = i
        else:
            break
            
    return answer