# Nothing can stop me and I never stop.

# tubson
# def tubson(n):
#     count = 0
#     for k in range(1, int(n ** 0.5)+1):  # +1 might be need
#         if n % k == 0:
#             count += 1
#             if k ** 2 != n:
#                 count += 1
#     return count <= 2

# # eng yaqin tubson
# n = int(input())
# while not tubson(n):
#     n -= 1
# print(n)

a = input()
n = reversed(list(map(int, list(a))))
q = ''
for k in n:
    q += str(k)

if int(a) > int(q):
    print(-1)
else:
    print(int(q))
