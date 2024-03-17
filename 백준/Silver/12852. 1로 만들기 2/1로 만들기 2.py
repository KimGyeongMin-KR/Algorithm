
N = int(input())

queue = [[0, N, []]]
ans = []

i= 0
num_visited = {N:1}

while queue:
    count, cur, visited = queue.pop(0)
    new_visited = visited[:]
    if cur == 1:
        new_visited.append(cur)
        ans.append([count, new_visited])
        break
    elif cur > 1:
        new_visited.append(cur)
        if cur % 3 == 0 and cur//3 not in num_visited:
            queue.append([count+1, cur//3, new_visited])
            num_visited[cur//3] = 1
        if cur % 2 == 0 and cur//2 not in num_visited:
            queue.append([count+1, cur//2, new_visited])
            num_visited[cur//2] = 1
        if cur-1 not in num_visited:
            queue.append([count+1, cur-1, new_visited])
            num_visited[cur-1] = 1

ans_sort = sorted(ans)
print(ans_sort[0][0])
for num in ans_sort[0][1]:
    print(num, end=" ")