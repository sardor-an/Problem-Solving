# def fuck_hanif(n):
#     if n > 26:
#         if n % 26 == 0:
#              return 1
#         else:
#             return n % 26
#     return n
# a = {}
# b = {}
# # creating the dict
# u = 1
# for i in range(97, 123):
#     a[u] = chr(i)
#     b[chr(i)] = u
#     u += 1
# print(a)

# k = int(input())
# s = input()
# ss = ''
# for i in s:
#     if i != '_':
#         f = fuck_hanif(b[i.lower()] + k)
#         if i.isupper():
#             ss += a[f].upper()
#         else:
#             ss += a[f]
#     else:
#         ss += '_'
# print(ss)
# a = {
#     15: 11,
#     14:18,
#     13: 9,
#     12: 19,
#     11: 5,
#     10: 22,
#     9: 48,
#     8: 43,
#     7: 33,
#     6: 26,
#     5: 44,
#     4:25,
#     3: 46,
#     2: 49,
#     1:32
# }
# print(a[int(input())])


# def fuck_hanif(n: int):
#     if n >= 100:i = 100
#     elif n <= 99 and n >= 20:i = 20
#     elif n <= 19 and  n >= 10: i = 10
#     elif n <= 9 and n >= 5: i = 5
#     else: i = 1
#     return i
# n = int(input())
# a = list(map(int, input().split()))
# def fuck_hanif_pro(n, a):
#     a = list(reversed(sorted(a)))
#     for k in range(len(a)):
#         if n >= a[k] :
#             return a[k]
# i = 0
# while n != 0:
#     m = fuck_hanif_pro(n, a)
#     i += n // m
#     n -= (n // m) * m
#     if n in a:
#         i += 1
#         break
# print(i)


x1, y1, x2, y2 = map(int, input().split())
m = 1 if y1 < y2 else -1
i = 0
flag = True
while flag:
    if x1 == x2:
        i += abs(y1 - y2)
        print('one', y1 - y2)
        flag = False
    elif y1 == y2:
        i += abs(x1 - x2)
        print('two')
        flag = False
    else:
        x1 += m
        y1 += m
        i += 1
        print('three')
print(int(i * 0.5))