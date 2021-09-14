import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [[INF] * (n+1)  for _ in range(n+1)]

for i in range(m):
  s,e,v = map(int, input().split())
  graph[s].append((v, e))
  distance[s][e] = v
for i in range(1, n+1):
  distance[i][i] = 0

# j에서 k를 갈때 i를 거쳐가는 길이를 조사.
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

for i in distance:
  print(i)