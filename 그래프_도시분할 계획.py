import heapq
import sys
input = sys.stdin.readline

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
parent = list(range(n+1))

edges = []
for i in range(m):
  s, e, cost = map(int, input().split())
  heapq.heappush(edges, (cost, s, e))

result = 0
maxValue = 0
count = n-2
while edges:
  cost, s, e = heapq.heappop(edges)
  if find(parent, s) != find(parent, e):
    union(parent, s, e)
    result += cost
    count -= 1
   
  if count == 0: break
print(result)

# 기본 아이디어는 최소신장트리를 구하는 알고리즘과 같지만
# 도시를 두개로 분할해야하기 때문에 최소신장트리를 구한 후 최대엣지를 하나삭제해주면
# 주어진 조건에 만족하는 답을 구할 수 있다.