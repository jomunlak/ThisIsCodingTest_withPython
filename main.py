# 아기 상어
from collections import deque
n = int(input())
graph = []
shark = (0, 0, 0)
for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(n):
    if data[j] == 9: shark = (i, j, 2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상 하 좌 우

def bfs(graph, shark):
  q = deque()
# king joong e
