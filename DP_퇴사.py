

n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
d = [0] * (n+2)
for i in range(n):
  a, b = map(int, input().split())
  t[i+1], p[i+1] = a, b

for i in range(n, 0, -1):
  if i + t[i] > n+1:
    d[i] = d[i+1]
  else:
    d[i] = max(d[i+1], d[i + t[i]] + p[i])

print(d[1])