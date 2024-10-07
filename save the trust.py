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



# s = 100
# m = 1
# n = 0
# r = 0
# while s > r:
#     r = m + n
#     print(r)
#     n = m
#     m = r
#     s -= 1

# --------------------------------------------------------------------------
# Mirror 5-6-7
    # B
# def check(y):
#     y = list(map(int, list(str(y))))
#     n = 0
#     while n <= len(y)-1:
#         if y.count(y[n]) > 1:
#             return False
#         else:
#             n += 1
#     return True
# y = int(input())+1
# while not check(y):
#     y += 1
# print(y)

# ------------------------------------------------------------------------- DAY 4
    # C
# l = int(input())
# k = list(map(int, input().split()))
# l = 9
# k = [3,1,2, 1,2,3, 2,3,1]

# temp = k[:3]*(l//3)
# t = 0
# for n in range(0, l):
#     if temp[n] != k[n]:
#         t += 1
# print(t)

# n, m = map(int, input().split())
# b = 0
# a = (m - b) ** 0.5
# while not a + (b**2) == n:
#    b += 1
# print(b)
  
# first 5 minutes for BETER STRUCTURE.



# Now, you do not know about calisthenis way(rest days, eating and training things ...). What should you do? - just find it by doing it. Analyze yourself


# nn = int(input())
# a = list(map(int, input().split()))
# c = 0
# for k in sorted(a)[1:]:
#   c += k - min(a)
# print(c)




# 10th grade 

# A
# x = int(input())
# y = int(input())
# diff = abs(x - y)

# if diff % 2 == 0:
#     print(diff // 2)
# else:
#     print(diff // 2 +1)

# B
# def tubson(n):
#     c = 0
#     for k  in range(1, int(n**0.5)+1):
#         if n % k == 0:
#             c += 1
#             if k * k != n:
#                 c += 1
#     return c

# n = int(input())+1
# c = 1
# while n != 0:
#     c += 1
#     if tubson(c) == 2:
#         n -= 1
# print(c)

# C
# n = int(input())
# a = sorted(list(map(int, input().split())))
# c = 0




# 10-sinf olimpiyada
n, m , a, b = map(int, input().split())
img = []
for i in range(0, n):
  img.append(input())
img_new = []
for k in img:
  f = ''
  for z in k:
    f += z*b
  img_new.append(f)
  
for k in img_new:
  for g in range(0, a):
    print(k)