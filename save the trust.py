# Kachok
# n, m = map(int, input().split())
# eggs = n
# day = 0
# while n != 0:
#     day += 1
#     if day == m or day % m == 0:
#         eggs += 1
#         n += 1
#     n -= 1
# print(day)

# Zapravka
# n, a, b = map(int, input().split())
# print(30 ** 0.5)



s = 100
m = 1
n = 0
r = 0
while s > r:
    r = m + n
    print(r)
    n = m
    m = r
    s -= 1