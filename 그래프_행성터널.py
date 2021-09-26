# 행성 터널
import heapq

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]
def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a<b: parent[b] = a
  else: parent[a] = b


n = int(input())
parent = list(range(n+1))
stars = [0] *(n+1)
for i in range(1,n+1):
  x, y, z = map(int, input().split())
  stars[i] = (x, y, z)

edges = []
for i in range(1, n):
  for j in range(i+1, n+1):
    nx = abs(stars[i][0] - stars[j][0])
    ny = abs(stars[i][1] - stars[j][1])
    nz = abs(stars[i][2] - stars[j][2])
    heapq.heappush(edges, (min(nx, ny, nz), i, j))


def kruskal():
  result = 0
  for cost, s, e in edges:
    if find(parent, s) != find(parent, e):
      result += cost
      union(parent, s, e)
  return result
answer = kruskal()
print(answer)