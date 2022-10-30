n,m = map(int,input().split())

coin = [int(input()) for _ in range(n)]
cnt = 0

for _ in range(n):
    c = coin.pop()
    cnt += m//c
    m %= c
    
print(cnt)