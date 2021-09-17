INF = 1e9
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]


for i in range(m):
  s, e, v = map(int, input().split())
  if v < graph[s][e]:
    graph[s][e] = v

for i in range(n+1):
  graph[i][i] = 0

for i in range(1, n+1):
  for row in range(1, n+1):
    for col in range(1, n+1):
      graph[row][col] = min(graph[row][col], graph[row][i] + graph[i][col])

for i in graph[1:]:
  for j in i[1:]:
    print(j if j != INF else 0, end = " ")
  print()



