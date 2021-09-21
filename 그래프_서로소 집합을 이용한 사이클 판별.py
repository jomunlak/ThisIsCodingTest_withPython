
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

v, e = map(int, input().split())  # vertex와 edge(union 연산))의 수
parent = [0] * (v+1)              # 부모 리스트

for i in range(1, v+1): parent[i] = i
# 부모 리스트 초기화

cycle = False
for i in range(e):
  a, b = map(int, input().split())
  if find(parent, a) == find(parent, b): 
    cycle = True
    break
  else:
    union(a, b)

if cycle: print("사이클 발생")
else: print("사이클 발생 안함")