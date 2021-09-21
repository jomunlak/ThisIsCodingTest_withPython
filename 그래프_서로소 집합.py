# 서로소 집합 자료구조 구현

def find(parent ,x):
  if parent[x] == x: return x
  else: return find(parent, parent[x])

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

for i in range(e):
  a, b = map(int, input().split())
  union(parent, a, b)

print("각 원소가 속한 집합: ", end ="")
for i in range(1, v+1):
  print(find(parent, i), end = " ")

print()
print("부모 테이블 내용 : ", end = "")
for i in parent:
  print(i, end = " ")