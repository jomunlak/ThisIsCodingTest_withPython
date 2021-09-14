import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
start = int(input())
graph = [[]for _ in range(n+1)]
distance = [INF] *(n+1)
q = [] 

def dijkstra(start):

  distance[start] = 0
  q.append((0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    print(dist, now, "확정")
    for v, e in graph[now]:
      nextDist = dist + v
      if nextDist < distance[e]:
        distance[e] = nextDist
        heapq.heappush(q, (nextDist, e))

for i in range(m):
  s,e,v = map(int, input().split())
  graph[s].append((v, e))

for i in graph:
  print(i)
print()
dijkstra(start)
