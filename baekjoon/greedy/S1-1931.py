# import sys; input = sys.stdin.readline;

tuple_list = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

cnt = 1
std = tuple_list[0]

for t in tuple_list[1:]:

    if t[1] < std[1]:
        std = t
    elif t[0] >= std[1]:
        std = t
        cnt += 1

print(cnt)



# 초기 답안 
# import sys; input = sys.stdin.readline;

# tuple_list = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

# cnt = 1
# std = tuple_list[0]

# for t in tuple_list[1:]:
#     if t[0] == std[0]:
#         if t[0] == std[1]:
#             std = t
#             cnt += 1
#     elif t[1] < std[1]:
#         std = t
#     elif t[0] >= std[1]:
#         std = t
#         cnt += 1
# print(cnt)