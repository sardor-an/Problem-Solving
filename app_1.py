# def snake_case(parts: list) -> str:
#     r = ''
#     for k in range(len(parts)):
#         e = '_'
#         if len(parts) - 1 == k:e = ''
#         r += f'{parts[k]}{e}'
#     return r
# def camelCase(parts: list) -> str:
#     r = ''
#     for k in range(len(parts)):
#         if k == 0:r += f'{parts[k]}'
#         else:r += f'{parts[k].title()}'
#     return r

# print(camelCase(['hello', 'world']))

# x, y = map(int, input().split())
# def fuck_hanif_0514(x,y):
#     r = y / (x * 1/100)
#     whole = int(r)
#     fraction = str(r - whole)[:4]
#     new_fraction = float(fraction)
#     if int(fraction[-1]) >= 5: new_fraction += 0.01
#     if new_fraction == 0:
#         return f'{whole}.00%'
#     return f'{whole}{str(new_fraction)[1:]}%'
# print(fuck_hanif_0514(x,y).replace(' ', '').strip(''))


# def calculate_percentage(x, y):

#   percentage = (x / y) * 100
#   formatted_percentage = f"{percentage:.2f}%"
#   return formatted_percentage

# # Example usage:
# x, y = 20, 5
# result = calculate_percentage(x, y)
# # print(result)  # Output: 400.00%

# print(f'{0.5457:.5f}%')

# n = int(input()[:-1]) / 100
# print(f'{int(100/n)}%')

def tub(n):
    a = 0
    for  k in range(1, int(n**0.5)+1):
        if n % k == 0:
            a += 1
            if k * k != n:a += 1
    if a > 2:return False
    return True
def chedd(a: list, n: int):
    if a[-1] % n == 0:
        a[-1] *= n
    else:
        a.append(n)
def fuck_hanif_1054(n):
    m = int(n ** 0.5)
    a = [1]
    i = 2
    if tub(n):return [1, n]
    while i <= m:
        if n % i == 0 and  tub(i):
            a.append(i)
            # chedd(a,i)
            f = n // i
            if tub(f):
                a.append(n//i)
                # chedd(a, n//i)
                n //= n // i
            n //= i
        else:
            i += 1
    return a[1:]
def collect(m: list):
    return sum(int, m)

n = int(input())
s = sum(map(int, str(n)))
g = 0
for k in fuck_hanif_1054(n):
    g += sum(map(int, str(k)))
print(1 if g == s else 0)


