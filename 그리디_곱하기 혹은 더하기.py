# 곱하기 혹은 더하기

data = input()
n = len(data)
result = int(data[0])
for i in range(1,n):
  x = int(data[i])
  result = max(result + x, result * x)
print(result)