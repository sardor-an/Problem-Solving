# print('Fuck Hanif')


    # HANIF IS GOING TO BE FUCKED
n = int(input())
r = 1
for k in range(n):
  a, b = map(int, input().split())
  c = range(a, b+1)
  if 0 not in c:r *= len(c)
  else:r *= len(c) - 1 
print(r % (10**9 + 7))