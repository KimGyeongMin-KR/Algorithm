### 정답 코드 반례 존재 ###
def solution(m):
    answer = 0
    m_idx = 0
    m.sort()
    for h in range(max(m)+1):
        
        if m[m_idx] < h:
            m_idx += 1
            
        if len(m[m_idx:]) >= h:
            answer = h
        else:
            break
            
    return answer

# 반례
# 입력 : [0,1,1,1,1,1,2,3,4]
# 정답 : 2
# 출력 : 4


# 보완한 답 0.002s
def solution(m):
    answer = 0
    m_idx = 0
    m.sort()
    for h in range(max(m)+1):
        
        if m[m_idx] < h:
            while m[m_idx] < h:
                m_idx += 1
                if m_idx == len(m)-1:
                    break
            
        if len(m[m_idx:]) >= h:
            answer = h
        else:
            break
            
    return answer


# 간단한 답 : 0.007s
def solution(m):
    
    h = 0
    
    for h in range(len(m), -1,-1):
        count = 0
        for num in m:
            if num >= h:
                count += 1
        if count >= h:
            return h


# 참고하면 좋을 코드 0.0002s
def solution(citations):
    citations.sort(reverse = True)
    for i, x in enumerate(citations) :
        if x <= i:
            return i
    return len(citations)