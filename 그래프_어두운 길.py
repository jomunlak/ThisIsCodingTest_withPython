# 어두운 길
def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]
def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a<b: parent[b] = a
  else: parent[a] = b

n, m = map(int, input().split())
parent = list(range(n))
sumValue = 0


edges = []
for _ in range(m):
  s, e, cost = map(int, input().split())
  sumValue += cost
  edges.append((cost, s, e))
edges.sort()

# 최소신장트리의 모든 edge값의 합을 리턴하는 메서드
def kruskal():
  result = 0
  for cost, s, e in edges:
    if find(parent, s) == find(parent, e): continue

    union(parent, s, e)
    result += cost
  return result

answer = sumValue - kruskal()
print(answer)