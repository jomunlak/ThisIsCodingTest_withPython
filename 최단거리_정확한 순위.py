import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
distance = [[INF] * (n+1)  for _ in range(n+1)]

for i in range(m):
  s,e = map(int, input().split())
  distance[s][e] = 1

for i in range(1, n+1):
  distance[i][i] = 0

# j에서 k를 갈때 i를 거쳐가는 길이를 조사.
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

count = 0
for i in range(1, n+1):
  res = 0
  for n in range(1, n+1):
    if distance[i][n] != INF or distance[n][i] != INF: # i보다 위에 있거나 아래에 있는것이 확실하다면 
      res += 1
  if res == n: # 모든 다른 사람에대해 위나 아래에 있는것이 확실하다면(범위는 모든 다른사람이지만 distance[i][i]를 포함하여 n과 비교)
    count += 1

print(count)
