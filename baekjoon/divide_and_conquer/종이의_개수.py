import sys

input = sys.stdin.readline
N = int(input())
answer = [0, 0, 0]
li = [list(map(int, input().split())) for _ in range(N)]

def checker(rstart, cstart, size):
    std = li[rstart][cstart]
    if size > 1:
        for ridx in range(rstart, rstart + size):
            for cidx in range(cstart, cstart + size):
                if li[ridx][cidx] != std:
                    resize = size//3
                    for i in range(3):
                        for j in range(3):
                            checker(rstart + i * resize, cstart + j * resize, resize)
                    return
    answer[std + 1] += 1
checker(0, 0, N)
print('\n'.join(map(str, answer)))