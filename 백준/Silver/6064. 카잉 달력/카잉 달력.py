T = int(input())

for _ in range(T):
    M, N, x, y = list(map(int, input().split()))
    step = min(M, N)
    s = set()
    c = 1
    tx, ty = 1, 1
    while True:
        if (x - tx) % M == (y - ty) % N:
            c += (x - tx) % M
            print(c)
            break
        tx = (tx + step)
        ty = (ty + step)
        tx = tx % M if tx > M else tx
        ty = ty % N if ty > N else ty
        xy = (tx, ty)
        if xy in s:
            print(-1)
            break
        s.add(xy)
        c += step
