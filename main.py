# 도시 분할 계획
# 서로소 집합 자료구조 구현
def find(parent ,x): # 경로압축이 적용된 find메서드
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b): # a 노드와 b 노드를 union한다.
  a = find(parent, a)
  b = find(parent, b)

  # 더 큰 번호의 노드가 작은 번호의 노드를 가리키도록 설정
  if a<b: parent[b] = a
  else: parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1): parent[i] = i

edges = []
for i in range(m):
  s, e, cost = map(int, input().split())
  edges.append((cost, s, e))
edges.sort()

result = 0
maxValue = 0
for cost, s, e in edges:
  if find(parent, s) == find(parent, e): continue
  else:
    union(parent, s, e)
    result += cost
    maxValue = cost

print(result - maxValue)
