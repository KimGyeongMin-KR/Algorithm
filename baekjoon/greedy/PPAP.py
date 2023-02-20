def checker(PPAP: str) -> bool:
    p_cnt = 1
    idx = 1
    if len(PPAP) == 1 and PPAP[0] == "P":
        return True

    if len(PPAP) < 4 or PPAP[0] != "P":
        return False
        
    while idx < len(PPAP):
        if p_cnt < 1:
            return False
            break

        if PPAP[idx] == "P":
            p_cnt += 1
            idx += 1
        elif PPAP[idx: idx + 2] == "AP":
            p_cnt -= 1
            idx += 2
        else:
            return False
            break
        
    if p_cnt == 1:
        return True
    return False
    
print("PPAP" if checker(input()) else "NP")