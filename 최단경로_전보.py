import heapq
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)] # 인접리스트
q = []
distance = [INF] * (n+1)
time_ = -1
count = 0

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((z, y))

def dijkstra(start):
  global time_
  global count

  distance[start] = 0
  q.append((0, start))
  
  while q:
    dist, now = heapq.heappop(q)
    print(dist, now)
    
    if distance[now] < dist:
      continue
    
    time_ = max(time_, dist)
    count += 1
    
    
    for v, e in graph[now]:
      nextDist = v + dist
      if nextDist < distance[e]:
        distance[e] = nextDist
        heapq.heappush(q, (nextDist, e))




dijkstra(c)

print(count -1, time_)
