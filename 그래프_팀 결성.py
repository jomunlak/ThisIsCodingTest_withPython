# 팀 결성(서로소 집합)

n, m = map(int, input().split())
parent= [0] * (n+1)
for i in range(n+1): parent[i] = i

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]
def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b: parent[b] = a
  else: parent[a] = b


for _ in range(m):
  opt, a, b = map(int, input().split())
  if opt == 0:
    union(parent, a, b)
  elif opt == 1:
    if find(parent, a) == find(parent, b): print("YES")
    else: print("NO")





