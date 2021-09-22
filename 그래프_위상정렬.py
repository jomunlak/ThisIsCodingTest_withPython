# 위상정렬
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1) # 진입차수 리스트
graph = [[] for _ in range(v+1)]

for i in range(e):
  s, e = map(int, input().split())
  graph[s].append(e)
  indegree[e] += 1

def topology_sort():
  result = []
  q = deque()

  for i in range(1, v+1): 
    if indegree[i] == 0: q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now) #삭제한 노드의 번호를 결과리스트에 삽입
    
    for g in graph[now]:
      indegree[g] -= 1
      if indegree[g] == 0: q.append(g)
  
  print(result)


topology_sort()

