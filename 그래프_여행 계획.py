# 여행계획
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n) ]
for i in range(n): 
  data = list(map(int, input().split()))
  graph[i] = [x if x != 0 else INF for x in data]
  graph[i][i] = 0
plan = list(map(int, input().split())) # 여행 계획

for i in range(n):
  for row in range(n):
    for col in range(n):
      graph[row][col] = min(graph[row][i] + graph[i][col], graph[row][col])

answer = "YES"
prev = plan[0]
for i in plan[1:]:
  if graph[prev-1][i-1] == INF:
    answer = "NO"
    break
  prev = i

for g in graph:
  print(g)

print(answer)

