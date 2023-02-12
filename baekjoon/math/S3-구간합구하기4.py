import sys
input = sys.stdin.readline

li = [0] * 100001
n,m = map(int,input().split())
for idx, item in enumerate(list(map(int,input().split()))):
    li[idx+1] = li[idx] + item

for _ in range(m):
    f, s = map(int,input().split())
    print(li[s] - li[f-1])