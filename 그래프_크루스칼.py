
# 크루스칼 알고리즘

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

v, e = map(int, input().split())  # vertex와 edge(union 연산))의 수
parent = [0] * (v+1)              # 부모 리스트

for i in range(1, v+1): parent[i] = i
# 부모 리스트 초기화

edges = [] # 모든 간선의 정보를 담은 리스트
result = 0

for i in range(e):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

for cost, v1, v2 in edges:
  if find(parent, v1) != find(parent, v2): 
    union(parent, v1, v2)
    result += cost

print(result) # 최소신장트리의 모든 edge의 cost를 합한 값