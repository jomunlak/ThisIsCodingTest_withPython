from collections import deque

n, m = map(int,input().split())

newMap = []

for i in range(n):
  newMap.append(list(map(int, input())))
visited = [[0]* m for _ in range(n)]
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0,0)) # 처음 위치 좌표를 나타내는 튜플
count = 1

while q: # 큐가 빌때까지
  
  if (n-1, m-1) in q:
    break

  loc = q.popleft()

  for i in range(4):
    x = loc[0] + dx[i]
    y = loc[1] + dy[i]
    if 0<= x < n:
      if 0<= y <m:
        if newMap[x][y] == 1:
          q.append((x, y))
          newMap[x][y] = newMap[loc[0]][loc[1]] + 1
  

  

print(newMap[n-1][m-1])
for i in newMap:
  print(i)

