from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)] # 간선 저장 2차원 리스트
distance = [-1] * (n + 1)

for i in range(m):
  src, dest = map(int, input().split())
  graph[src].append(dest)
  # graph[1 ~ n]에 각 노드에 인접한 노드의 번호들이 저장되어있다. 

q = deque()
q.append(x) # 시작지점 정하기.
distance[x] = 0

while q:

  now = q.popleft()

  for next_node in graph[now]:
    if distance[next_node] == -1:
      #아직 방문하지 않은 노드라면
      distance[next_node] = distance[now] + 1 
      q.append(next_node) 
    else:
      continue

sortQ = []
for i in range(len(distance)):
  if distance[i] == k:
    sortQ.append(i)
if len(sortQ) == 0:
  sortQ.append(-1)
  
sortQ.sort()
for i in sortQ:
  print(i)  

