# Kachok
n, m = map(int, input().split())
eggs = n
day = 0
while n != 0:
    day += 1
    if day == m or day % m == 0:
        eggs += 1
        n += 1
    n -= 1
print(day)