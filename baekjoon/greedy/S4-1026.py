input()
l1 = sorted(map(int, input().split()))
l2 = sorted(map(int, input().split()), reverse = True)
print(sum([x*y for x,y in zip(l1, l2)]))