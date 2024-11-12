# #1 - 0004
# # n, p = map(int, input().split())
# # print(n*p)

# #2 - 0010
# # n = int(input())
# # a,b,c = map(int, input().split())
# # if a + b + c >= n:print('Yes')
# # else: print('No')

# #3 - 0019
# # n, k = map(int, input().split())
# # print(k // n)

# #4 - 0023
# # print(input()[-1])

# #5 - 0043
# # a,b = map(int, input().split())
# # print(b, a)

# #6 - 0020
# # a, b = map(int, input().split())
# # print(b % a)

# #7 - 0022
# # print(input()[0])


# #8 - 0707
# # print(input())

# #9 - 0059
# # print(int(input())**2)

# #10 - 0008
# # a = list(map(int, input().split()))
# # print(sum(a)-max(a), sum(a)-min(a))

# #11 - 0058 $
# # print(7-int(input()))

# #12 - 0013
# #n, k = map(int, input().split())
# #if n == 0:print(1)
# #else: print(k+1) # karantinga tiqildi.Chunki shartda eng kamida


# #13 - 0372
# # a,b,c = map(int, input().split())
# # print(max(max(a,b), c))

# #14 - 0011
# # n = int(input())
# # print(max(sorted(list(map(int, input().split())))[:-1]))

# #15 - 0119
# # n = int(input())
# # if n % 4 == 0:print(n//4 * 2)
# # else:print(-1)

# #16 - 
# # a,b,c = map(int, input().split())
# # def parta(n):
# #   if n % 2 == 0: return n // 2
# #   return n // 2 + 1
# # print(parta(a)+parta(b)+parta(c))


# #17 - 0009
# # n = int(input())
# # m = list(map(int, input().split()))
#     # python version
# # i = 0
# # while m.count(m[i]) == 2:
# #   i += 1
# # print(m[i])

#     # logic versino
# # a = list(range(0, 101, 2)) # 101 * 2
# # for i in m:
# #     a[i] += 1

# # i = 0
# # while a[i] % 2 == 0:
# #     i += 1
# # print(i)

#     # god version
# # def find_single_number(nums):
# #     result = 0
# #     for num in nums:
# #         result ^= num
# #     return result


# #18 - 0138
# # x = int(input())
# # print(x**4 * (x + 8) + x**2 * (3 - 5*x) + x -12)

# #19 - 
# # n = int(input())
# # print(n*(n-3)//2)

# #20 - 0860
# # a,b = map(int, input().split())
# # f = list(range(a, b+1))
# # print(len(f))

# #21 - 0201
# # n = int(input())
# # if n % 2 == 1:
# #     print(n // 2 + 1)
# # else:
# #     print((n-2) // 2 + 2)

# #22 - 0045
# # n = int(input())
# # if n % 2 == 0:
# #   print((n + 1)*(n//2))
# # else:
# #   print((n+1)*(n//2) + (n+1)//2)

# #23 - 0082
# # n = int(input())
# # if n % 2 == 1:print('First player')
# # else:print('Second player')

# #24 - 0005
# # n = int(input())
# # if n != 0:
# #     def _(n):
# #         a = 0
# #         for k in range(1, int(abs(n)**0.5) + 1):
# #             if abs(n) % k == 0:
# #                 a += 1
# #                 if k ** 2 != abs(n):
# #                     a += 1

# #         return a
# #     if n ** 0.5 == int(abs(n)**0.5):
# #         print(_(n) + 1)
# #     else:print(_(n))
# # else:print(-1)

# #25 - 0024
# # h1,m1,s1 = map(int, input().split())
# # h2,m2,s2 = map(int, input().split())
# # total_s1 = (h1 * 3600) + (m1 * 60) + s1
# # total_s2 = (h2 * 3600) + (m2 * 60) + s2
# # print(total_s2 - total_s1)

# #26 - 1092
# # n = int(input())
# # if n % 2 == 0:print(n)
# # else: print(n*2)

# #27 - 0374
# # a = list(map(int, input().split()))
# # print(max(a) - min(a))

# #28 - 0938
# # a = int(input())
# # f = (10*27+22-9/3)*7-2022-1-a
# # print(int(f))

# #29 - 0812
#     # pythons version
# # print(int(f'{input()}', 16) % 2)

#     # version of me
# # a = input()
# # base = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
# # r = 0
# # i = 0
# # for k in a[::-1]:
# #     if not k.isdigit():
# #         r += base[k] * 16 ** i
# #     else:r += int(k) * 16  ** i
# #     i += 1
# # print(r % 2)

# #30 - 0071
# # print(int(input()//2 + 1))

# #31 - 0076
# # a = sum(list(map(int, input().split())))
# # s = int(input())
# # if s - a >= 0:
# #     print(s - a)
# # else:
# #     print(0)

# #32 - 0265
# # a,b = map(int, input().split())
# # print(a,b)

# #$31 - 0479
# # n = int(input())
# # if (n / 100) == int(n / 100):
# #     print(int(n / 100))
# # else:
# #     print(n / 100)


# #32 -
# # a,b,c = list(map(int, input().split())) 
# # x = 3
# # a = [1,2,3,4,3,2,1]
# # print(a[1],a[-2] )




# #33 - floyd uchburchagi       ---------wasted
# # def floyd_triangle(n):
# #     number = 1
# #     for i in range(1, n+1):
# #         for j in range(1, i+1):
# #             print(number, end=" ")
# #             number += 1
# #         print()

# # # Example usage:
# # n = 1502
# # floyd_triangle(n)

# #34
# # n = input()
# # s = int(n)
# # if not s < 38:
# #     if int(n[1]) <= 5:
# #         if 5 - int(n[1]) < 3:s += 5 - int(n[1])
# #     else:
# #         if 10 - int(n[1]) < 3:s += 10 - int(n[1])
# #     print(s)
# # else:
# #     print(int(n))


# #35
# # t = int(input())
# # T = int(input())
# # r = (t + T) % 24
# # if t + T == 24:print(0)
# # else:print(r)

# # def ok(n):
# #     s = int(n)
# #     a = []
# #     for k in range(100, s):
# #         if int(str(k)[1:]) + k == s:a.append(k)
# #     if a:
# #         if len(a) == 1:print(a[0])
# #         else:
# #             print(f'{a[0]} {a[1]}')

# # ok(int(input()))


# #
# # n = int(input())
# # x = 0
# # def is_this(n):
# #     s = 0
# #     for k in range(1, int(n**0.5)+1):
# #         if n % k == 0:
# #             s += 1
# #             if k ** 2 != k:s += 1
# #     return s <= 2

# # for k in range(1, n+1):
# #     if is_this(k): x += 1

# # if x % 2 == 0:print('Ali')
# # else:print('Bobur')

# # def sieve_of_eratosthenes(n):
# #   """
# #   Finds all prime numbers up to a given limit `n` using the Sieve of Eratosthenes.

# #   Args:
# #     n: The upper limit for finding prime numbers.

# #   Returns:
# #     A list of prime numbers up to `n`.
# #   """

# #   prime = [True for i in range(n+1)]
# #   p = 2
# #   while (p * p <= n):
# #     if (prime[p] == True):
# #       for i in range(p * p, n+1, p):
# #         prime[i] = False
# #     p += 1

# #   prime[0]= False
# #   prime[1]= False

# #   prime_numbers = []
# #   for p in range(n+1):
# #     if prime[p]:
# #       prime_numbers.append(p)

# #   return len(prime_numbers)

# # # Example usage:
# # limit = int(input())
# # primes = sieve_of_eratosthenes(limit)
# # if primes % 2 == 0:print('Ali')
# # else: print('Bobur')

# # s = input()

# # index = 0
# # var0 = 1
# # var1 = 1
# # def puu(s, var):
# #     _1_is_saved = 0
# #     _0_is_saved = 0
# #     _0_is_pre_saved = 0
# #     for i in s:
# #         if int(i) == 1:
# #             _1_is_saved = 1
# #         else:
# #             _0_is_saved += 1
# #         if not _1_is_saved:
# #     	    _0_is_pre_saved += 1

# #         if _0_is_saved != _0_is_pre_saved:
# #             var = 0
# #             break
# # puu(s, var0)
# # puu(s[::-1], var1)
# # if var0 and var1:print('YES')
# # else:print('NO')

# # v = int()
# # if v >= 2 and v <= 7:print('Econom 105K')
# # elif v == 8 or v == 9:print('Business 140K')
# # else:print('VIP 210K')

# # n, k = map(int, input().split())
# # r = 0
# # if n == 0:print(0)
# # else:
# #     for i in range(n):
# #         r += k**i
# #     print(r % 10e9+7)
# # n, k = map(int, input().split())
# # r = 0
# # if n == 0:print(0)
# # else:
# #   print(int((k**n - 1) / (k-1)))

# # t = int(input())
# # a = []
# # for k in range(t):
# #   i = int(input())
# #   a.append(i*i)

# # for b in a:
# #   print(b)

# # def check(n: int) -> bool:
# #     if n % (sum(list(map(int, str(n)))) ** 2) == 0:
# #         return True
# #     return False

# # n = int(input())
# # x = 0
# # b = 0
# # while n != b:
# #     x += 1
# #     if check(x):
# #         b += 1
    
# # print(x)

# # a = input()
# # f_1 = 0
# # for i in range(len(a)):
#     # if a[i] == 1:
#     #     f_1 = i
#     #     print(f_1)
#     #     break
#     # print(a[i])
# # if a[i:].count('33'):print('omadsiz chipta')
# # else:print('omadli chipta')


# #36
# # def number(n):
# #     for k in range(100, n+1):
# #         if int(k) + int(str(k)[1:]) == n:
# #             print(k, end=' ')
# # number(126)


# # a = '011111000'
# # copy_a = ''
# # one = False
# # for i in range(len(a)):
# #     if a[i] == '1':
# #         one = True
# #         copy_a += '1'
# #     else:
# #         if a[i] == '0' and one and a[i-1] != '0':
# #             copy_a += '0'

# # if '0' in copy_a[:-1]:print('NO')
# # else:print('YES')



# # n = int(input())
# # nums = list(map(int, input().split()))
# # s = ''
# # def check(n):
# #     # n*(n+1) // 2

# #     for i in range(0, n//2 + 2):
# #         if n == (i * (i + 1))//2:
# #             return True
# #     return False
    
# # print(check(5))
# # for k in nums:
# #     if check(k):s += '1'
# #     else: s += '0'
# # print(s)


# # a = int(input())
# # for k in range(a):
# #   print((int(input())**2 + 1)*k)


# # def check(n, k):
# #     if k == n*(n+1)//2:return '1'
# #     return '0'
# # s = ''
# # n = int(input())
# # for k in range(n):
# #   a, b = map(int, input().split())
# #   s += check(a,b)
# # print(s)
            
# #93 - 0573
# # n, t = map(int, input().split())
# # print((24-n)+t)

# #94
# # print('0001100'.strip('0'))
  	

# #95
# # n = int(input())
# # s = 0
# # for k in range(1, n+1):
# #   s += (k*(k+1))//2
# # print(s)

# #106 - 0612
# # d = {}
# # for i in range(1, 27):
# #     d[i] = chr(ord('A') + i - 1)
# # r = 0
# # a, b = map(str, input().split())
# # for k, i in d.items():
# #     if a == i: r += k
# #     if b == i: r += k
# # print(r)

# #107 - 0215
# # n = int(input())
# # an = ((2**((2*n) + 1)) * 3) - 2**(n+1)
# # if an % 5 == 0:print('A')
# # else: print('B')

# #0514 
# # x, y = map(int, input().split())
# # print((y/x) * 100)

# # a = int(input())

# # if a >= 0:
# #     a_n = str(bin(a))[2:]
# #     print(a_n.zfill(32))
# # else:
# #     a_n = str(bin(a))[3:]
# #     len_an = len(a_n)
# #     p1 = a_n
# #     p2 = '1'*(31-len_an)
# #     print(f'{p2}{p1}1')


# def tub(n):
#     a = []
#     for k in range(1, int(n**0.5)+1):
#         if n % k == 0:
#             a.append(k)
#             if k ** 2 != n:
#                 a.append(n // k)
#     return a

# def tub_ajrat(n):
#     i = 2
#     while True:
#         if n % i == 0 and len(tub(i)) > 2:
#             n = n // i
#             if n % i != 0 and len(tub(n)) > 2:
    
#                 i += 1


#     l = int(input())
#     a = sorted(list(map(int, input().split())))
#     r = 0
#     i = 0
#     while i < l:
#         if i+1 < l-1 and a[i] == a[i+1]:
#             r += 1
#             i += 2
#         else:
#             i += 1
#     print(r)


# # from math import log2
# # print(log2(int(input())))

# n = int()
# # a = reversed(sorted(list(map(int, input().split()))))
# a = list(map(int, input().split()))
# i, j = 0, n



# Creating a dictionary with numbers as keys and their corresponding words as values


# base = {
#     0: "",
#     1: "bir",
#     2: "ikki",
#     3: "uch",
#     4: "to'rt",
#     5: "besh",
#     6: "olti",
#     7: "yetti",
#     8: "sakkiz",
#     9: "to'qqiz",
#     10: "o'n",
#     20: "yigirma",
#     30: "o'ttiz",
#     40: "qirq",
#     50: "ellik",
#     60: "oltmish",
#     70: "yetmish",
#     80: "sakson",
#     90: "to'qson",
#     100: "bir yuz",
#     1000: "bir ming"
# }

# n = int(input())
# k = n
# if n == 1000:print(base[n])
# elif n == 0:print('nol')
# else:
#     yuz = n // 100
#     n -= yuz*100
#     on = n // 10
#     bir = n - (on * 10)
#     n -= bir
#     if k >= 100:
#         s = f'{base[yuz]} yuz {base[n]} {base[bir]}'
#     elif k < 10:s = f'{base[bir]}'
#     else:
#         s = f'{base[n]} {base[bir]}'
#     print(s.replace("  ", " "))


# Dictionary for basic numbers in Uzbek
# bla = int(input())
# a = map(int, input().split())
# s = ''
# for x in a:
#     if (1+8*x) ** .5 == int((1+8*x) ** .5):s += '1'
#     else:s += '0'
# print(s)

# a,b = map(int, input().split())
# r = 0
# for  k in range(a, b+1):
#   print(k)
#   if k % 3 == 0 and k % 7 != 0:
#     r += k
# print(k)
from math import ceil
x, y = map(int, input().split())
r = y/x * 100
unw = r - int(r)
if str(unw)[4] >= 5:
    f = str(unw)[:3]
    ...

