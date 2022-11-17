def solution(s):
    std = 0
    for i in s:
        std += 1 if i=='(' else -1
        if std < 0:
            return False
    return True if std == 0 else False