# print('Fuck Hanif')


    # HANIF IS GOING TO BE FUCKED
# n = int(input())
# r = 1
# for k in range(n):
#   a, b = map(int, input().split())
#   c = range(a, b+1)
#   if 0 not in c:r *= len(c)
#   else:r *= len(c) - 1 
# print(r % (10**9 + 7))




    # REALLY SHE WANT TO BE FUCKED
# def fuck_hanif_30(n):
#     i = 1
#     while not(checker(i) and i % n == 0):
#         i += 1
#     return i
# a = list(map(lambda x:0, range(1, 501) ))
# def checker(n):
#     return sum(map(int, str(n))) == 9 * str(n).count('9')
# def fuck_hanif_30_pro(n):
#     i = 1
#     while True:
#         if a[n] != 0:return a[n]
#         else:
#             if checker(n):
#                 return n
#             else:
#                 bin_i = str(bin(i))[2:].replace('1', '9')
#                 if int(bin_i) % n == 0:
#                     a[n] = int(bin_i)
#                     return int(bin_i)
#                 i += 1
# for k in range(10000):
#     print(fuck_hanif_30_pro(499))

# n, k = map(int, input().split())
# # nx + k
# def tool(n, k):
#     ...
# i = 1
# result = 0
# while result != n:
#     ex = i*n + k
#     if (ex * 4) % (n - 1) == 0:
#         ex = (ex * 4) // (n - 1) + k
#         if (ex*4) % (n-1) == 0:
#             ex = (ex*4) // (n-1)
#     else:
#         i += 1

# x, y = map(int, input().split())
# def fuck_hanif(y):
#     global r
#     if r - y < 0:return 0
#     return r - y
# i = 0
# r = 0
# while r != 100:
#     fuck_hanif(y)
#     r += x
#     fuck_hanif(y)
#     fuck_hanif(y)

#     i += 1
# print(i)



# def fuck_hanif_yaxlitla(s):
#     s = s / 4
#     if s - int(s) > 0 and s - int(s) < 0.5:return int(s)
#     else: return int(s) + 0.5

# a = fuck_hanif_yaxlitla(sum(map(int, input().split())))
# b = fuck_hanif_yaxlitla(sum(map(int, input().split())))
# c = float(input())
# d = float(input())
# r = (a+b+c+d) / 4
# print(r)
# if r - int(r) > 0.5:print(int(r)+1)
# else:print(int(r) + 0.5)



# n = int(input())
# a = sorted(list(map(int, input().split())))
# r = 0
# i = None
# for b in range(1, 5+1):
#     if a.count(b) > r:
#         r = a.count(b)
#         i = b
# print(i)



# s, t = map(int, input().split())
# a,b = map(int, input().split()) # daraxt joylashuvi
# m, n = map(int, input().split()) # to'kilgan olmalar va apelsinlar soni
# m_olma_d = map(int, input().split()) # olmalarning har biri uchun d qiymatlar
# n_apelsin_d = map(int, input().split()) # apelsinlarning har biri uchun d qiymatlar
# apelsin, olma = 0, 0
# eshak = range(s, t+1)
# for k in m_olma_d:
#   if a + k in eshak:
#    	olma += 1
# for k in n_apelsin_d:
#   if b + k in eshak:
#     apelsin += 1
# print(olma)
# print(apelsin)


# a,b = map(int, input().split())
# h = int((2*a)/b)
# if a > (h*b)/2:print(h+1)
# else:print(h)


def fuck_hanif_tub_ajrat(n):
    def tub(f):
        result = 2
        for k in range(2, int(f**0.5)+1):
            if f % k == 0:
                result += 1
                if k * k != f:
                    result += 1
        return result > 2
    def checker(a: list,n: int):
        if a[-1] == n:
            a[-1] = a[-1] * n
        else:a.append(n)
    a = [1]
    m = n
    i = 2
    while i <= int(n ** 0.5)+1:
        if not tub(i) and  m % i == 0:
            a.append(i)
            # checker(a, i)

            if m // i not in a:
                a.append(m // i)
                # checker(a, m // i)/
                m //= (m // i)
            else:
                m //= i
        else:
            i += 1
    return a[1:]

# n = int(input())
# r = range(1, n+1)

# i = 0
# for k in fuck_hanif_tub_ajrat(n+1):
#     if k not in r:
#         i = k
#         break
# print(k)

# print(fuck_hanif_tub_ajrat(198))


# t,s,v = map(float, input().split())
# r = (s / t) - v
# if r - int(r) == 0:print(int(r))
# else:print(r)


# a = list(map(int, input().split()))

# if len(a) == 2:
#     print(sum(a))
# else:
#     c = int(input())
#     print(a[0]*c)

def most_near(n: int, a: list):
    m = abs(a[0] - n)
    i = a[0]

    for k in a:
        if abs(k - n) < m:
            i = k
    return i




# n = int(input())
a = [100, 20, 10, 5, 1]
# c = 0
# while n != 0:
#     f = most_near(n, a)
#     d = n // f
#     c += d
#     print(c)
#     n -= d * f
# print(c)

print(most_near(25, a))