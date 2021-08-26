import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)] 
unions = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상하좌우

q =deque()

def bfs(row, col):
  global l, r

  if visited[row][col] != 0:
    return
  q.append((row, col))
  visited[row][col] = 1

  tmp_union = []
  tmp_union.append((row, col))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx<n and 0<= ny <n and visited[nx][ny] == 0:
        if l<= abs(graph[x][y] - graph[nx][ny])<= r:
          q.append((nx, ny))
          tmp_union.append((nx, ny))
          visited[nx][ny] = 1
  unions.append(tmp_union)

prev = [[0 for _ in range(n)] for _ in range(n)]# 직전 인구이동 후의 그래프
count = 0 #인구이동 횟수

while True: 
  # 인구이동 실행전 상태 저장
  for i in range(n):
    for j in range(n):
      prev[i][j] = graph[i][j]

  # 연합 목록과 방문기록 초기화
  unions.clear()
  for i in range(n):
    for j in range(n):
      visited[i][j] = 0
  
  for i in range(n):
    for j in range(n):
      bfs(i, j)
      # 그래프에서 연합을 형성한다.


  # 각 연합에대해 인구이동 실행
  for union in unions:
    sum_value = 0
    div_value = len(union)
    for x, y in union:
      sum_value += graph[x][y]
    res = int(sum_value / div_value)
    for x, y in union:
      graph[x][y] = res

  same = True
  # 인구이동을 실행한 후에도 변하지 않았다면 실행종료
  for i in range(n):
    for j in range(n):
      if prev[i][j] != graph[i][j]:
        same = False
  if same:
    break

  count += 1
    

print(count)