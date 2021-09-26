# 최종 순위
from collections import deque

def topology(indegree, graph, n):
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0: q.append(i)
  if len(q) == 0: return "IMPOSSIBLE"
  elif len(q) >= 2: return "?"

  result = []
  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0: 
        q.append(i)
        
    if len(result) == n: break
    if len(q) == 0: return "IMPOSSIBLE"
    elif len(q) >= 2: return "?"
  tmp = ""
  for i in result: tmp += str(i) + " "
  return tmp

tc = int(input())
for _ in range(tc):
  n = int(input())
  rank = list(map(int, input().split()))
  m = int(input())
  indegree = [0] * (n+1)
  graph = [[False] * (n+1) for _ in range(n+1)]
  change = []
  for _ in range(m): change.append(tuple(map(int, input().split())))
  for i in range(n):
    for j in range(i+1, n):
      graph[rank[i]][rank[j]] = True
      indegree[rank[j]] += 1
  
  for s, e in change:
    if graph[s][e]:
      graph[s][e] = False
      graph[e][s] = True
      indegree[e] -= 1
      indegree[s] += 1
    else:
      graph[e][s] = False
      graph[s][e] = True
      indegree[s] -= 1
      indegree[e] += 1
  
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0: q.append(i)  
  
  result = []
  for i in range(n):
    if len(q) == 0: 
      result = "IMPOSSIBLE"
      break
    elif len(q) >= 2: 
      result = "?"
      break

    now = q.popleft()
    result.append(now)    
    
    for i in range(1, n+1):
      if graph[now][i]:
        indegree[i] -= 1
        if indegree[i] == 0:
          q.append(i)
  if result == "IMPOSSIBLE":
    print(result)
  elif result == "?":
    print(result)
  else:
    for i in result:
      print(i, end =" ")
    print()

