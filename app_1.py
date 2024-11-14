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


def calculate_percentage(x, y):

  percentage = (x / y) * 100
  formatted_percentage = f"{percentage:.2f}%"
  return formatted_percentage

# Example usage:
x, y = 20, 5
result = calculate_percentage(x, y)
# print(result)  # Output: 400.00%

print(f'{0.5457:.5f}%')