# 문자열 뒤집기

data = input()
prev = data[0]

result0 = 0
result1 = 0

for d in data[1:]:
  if d != prev:
    if prev == '0': result0 += 1
    else: result1 += 1
  prev = d

if prev == '0': result0 += 1
else: result1 += 1
print(min(result0, result1))

