from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)] # 
cost = [0] * (n+1)      # 소요시간 리스트
time_ = [0] * (n+1)     # 각 수업마다 걸리는 최소시간
indegree = [0] * (n+1)  # 진입차수 리스트
q = deque()

for i in range(1, n+1):
  data = list(map(int, input().split()))
  cost[i] = data[0]
  for c in data[1:-1]:
    graph[c].append(i)
    indegree[i] += 1

# 차수가 0인 노드들을 큐에 삽입
for i in range(1, n+1):
  if indegree[i] == 0: 
    q.append(i)
    time_[i] = cost[i] # 차수가 0인 수업은 최소시간이 그 자체의 소모시간

while q:
  now = q.popleft()
  for g in graph[now]:
    time_[g] = max(cost[g] + time_[now], time_[g])
    indegree[g] -= 1
    if indegree[g] == 0: q.append(g)

print(time_)