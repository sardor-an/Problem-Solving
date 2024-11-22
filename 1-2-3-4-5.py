def fuck_hanif(n):
    if n > 26:
        if n % 26 == 0:
             return 1
        else:
            return n % 26
    return n
a = {}
b = {}
# creating the dict
u = 1
for i in range(97, 123):
    a[u] = chr(i)
    b[chr(i)] = u
    u += 1
print(a)

k = int(input())
s = input()
ss = ''
for i in s:
    if i != '_':
        f = fuck_hanif(b[i.lower()] + k)
        if i.isupper():
            ss += a[f].upper()
        else:
            ss += a[f]
    else:
        ss += '_'
print(ss)