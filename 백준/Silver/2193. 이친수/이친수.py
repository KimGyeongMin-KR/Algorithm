N = int(input())
l = [1, 1] + [0] * N
for i in range(2, N + 1):
    l[i] = l[i-1] + l[i-2]
print(l[N-1])