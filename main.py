# Viloyat 2023 11-sinf

# def manhattan(n):
#     """ |a-c| + |b-d| """

#     xy_pairs = []
#     for k in range(n):
#         x,y = map(int, input().split())
#         xy_pairs.append([x,y])
#     r_min, r_max = 0,0
#     for i in xy_pairs:
#         for j in xy_pairs:
#             if abs(i[0] - j[0]) + abs(i[1] - j[1]) > ...:
#                 ...
    

    
# print(manhattan(4))
print(...)


n = int(input())
m = list(map(int, input().split()))
a = list(range(0, 101, 2))


for k in range(n+1):
    a[k] += 1
print(a)