#1 - 0004
# n, p = map(int, input().split())
# print(n*p)

#2 - 0010
# n = int(input())
# a,b,c = map(int, input().split())
# if a + b + c >= n:print('Yes')
# else: print('No')

#3 - 0019
# n, k = map(int, input().split())
# print(k // n)

#4 - 0023
# print(input()[-1])

#5 - 0043
# a,b = map(int, input().split())
# print(b, a)

#6 - 0020
# a, b = map(int, input().split())
# print(b % a)

#7 - 0022
# print(input()[0])


#8 - 0707
# print(input())

#9 - 0059
# print(int(input())**2)

#10 - 0008
# a = list(map(int, input().split()))
# print(sum(a)-max(a), sum(a)-min(a))

#11 - 0058 $
# print(7-int(input()))

#12 - 0013
#n, k = map(int, input().split())
#if n == 0:print(1)
#else: print(k+1) # karantinga tiqildi.Chunki shartda eng kamida


#13 - 0372
# a,b,c = map(int, input().split())
# print(max(max(a,b), c))

#14 - 0011
# n = int(input())
# print(max(sorted(list(map(int, input().split())))[:-1]))

#15 - 0119
# n = int(input())
# if n % 4 == 0:print(n//4 * 2)
# else:print(-1)

#16 - 
# a,b,c = map(int, input().split())
# def parta(n):
#   if n % 2 == 0: return n // 2
#   return n // 2 + 1
# print(parta(a)+parta(b)+parta(c))


#17 - 0009
# n = int(input())
# m = list(map(int, input().split()))
    # python version
# i = 0
# while m.count(m[i]) == 2:
#   i += 1
# print(m[i])

    # logic versino
# a = list(range(0, 101, 2)) # 101 * 2
# for i in m:
#     a[i] += 1

# i = 0
# while a[i] % 2 == 0:
#     i += 1
# print(i)

    # god version
# def find_single_number(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result


#18 - 0138
# x = int(input())
# print(x**4 * (x + 8) + x**2 * (3 - 5*x) + x -12)

#19 - 
# n = int(input())
# print(n*(n-3)//2)

#20 - 0860
# a,b = map(int, input().split())
# f = list(range(a, b+1))
# print(len(f))

#21 - 0201
# n = int(input())
# if n % 2 == 1:
#     print(n // 2 + 1)
# else:
#     print((n-2) // 2 + 2)

#22 - 0045
# n = int(input())
# if n % 2 == 0:
#   print((n + 1)*(n//2))
# else:
#   print((n+1)*(n//2) + (n+1)//2)

#23 - 0082
# n = int(input())
# if n % 2 == 1:print('First player')
# else:print('Second player')

#24 - 0005
# n = int(input())
# if n != 0:
#     def _(n):
#         a = 0
#         for k in range(1, int(abs(n)**0.5) + 1):
#             if abs(n) % k == 0:
#                 a += 1
#                 if k ** 2 != abs(n):
#                     a += 1

#         return a
#     if n ** 0.5 == int(abs(n)**0.5):
#         print(_(n) + 1)
#     else:print(_(n))
# else:print(-1)

#25 - 0024
# h1,m1,s1 = map(int, input().split())
# h2,m2,s2 = map(int, input().split())
# total_s1 = (h1 * 3600) + (m1 * 60) + s1
# total_s2 = (h2 * 3600) + (m2 * 60) + s2
# print(total_s2 - total_s1)

#26 - 1092
# n = int(input())
# if n % 2 == 0:print(n)
# else: print(n*2)

#27 - 0374
# a = list(map(int, input().split()))
# print(max(a) - min(a))

#28 - 0938
# a = int(input())
# f = (10*27+22-9/3)*7-2022-1-a
# print(int(f))

#29 - 0812
    # pythons version
# print(int(f'{input()}', 16) % 2)

    # version of me
# a = input()
# base = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
# r = 0
# i = 0
# for k in a[::-1]:
#     if not k.isdigit():
#         r += base[k] * 16 ** i
#     else:r += int(k) * 16  ** i
#     i += 1
# print(r % 2)

#30 - 0071
# print(int(input()//2 + 1))

#31 - 0076
# a = sum(list(map(int, input().split())))
# s = int(input())
# if s - a >= 0:
#     print(s - a)
# else:
#     print(0)

#32 - 0265
# a,b = map(int, input().split())
# print(a,b)

#$31 - 0479
# n = int(input())
# if (n / 100) == int(n / 100):
#     print(int(n / 100))
# else:
#     print(n / 100)


#32 -
# a,b,c = list(map(int, input().split())) 
# x = 3
# a = [1,2,3,4,3,2,1]
# print(a[1],a[-2] )




#33 - floyd uchburchagi       ---------wasted
# def floyd_triangle(n):
#     number = 1
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(number, end=" ")
#             number += 1
#         print()

# # Example usage:
# n = 1502
# floyd_triangle(n)

#34
# n = input()
# s = int(n)
# if not s < 38:
#     if int(n[1]) <= 5:
#         if 5 - int(n[1]) < 3:s += 5 - int(n[1])
#     else:
#         if 10 - int(n[1]) < 3:s += 10 - int(n[1])
#     print(s)
# else:
#     print(int(n))


#35
# t = int(input())
# T = int(input())
# r = (t + T) % 24
# if t + T == 24:print(0)
# else:print(r)

# def ok(n):
#     s = int(n)
#     a = []
#     for k in range(100, s):
#         if int(str(k)[1:]) + k == s:a.append(k)
#     if a:
#         if len(a) == 1:print(a[0])
#         else:
#             print(f'{a[0]} {a[1]}')

# ok(int(input()))


#
n = int(input())
x = 0
def is_this(n):
    s = 0
    for k in range(1, int(n**0.5)+1):
        if n % k == 0:
            s += 1
            if k ** 2 != k:s += 1
    return s <= 2

for k in range(1, n+1):
    if is_this(k): x += 1

if x % 2 == 0:print('Ali')
else:print('Bobur')