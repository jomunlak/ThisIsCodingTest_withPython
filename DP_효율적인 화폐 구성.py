
n, m = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [0] * 10001
for c in coin:  d[c] = 1

for i in range(1,m+1):
  for c in coin:
    prev = i - c
    if prev >= 1 and d[prev] != 0:
      d[i] = d[prev] + 1 if d[i] == 0 else min(d[i], d[prev] +1)

print(d[m] if d[m] != 0 else -1)


