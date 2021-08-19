from collections import deque

n, k = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(n)] 
# 리스트 컴프리헨션을 이용한 이차원 리스트 입력

s, r, c = map(int, input().split())
# s초 뒤에 (x, y)에 있는 바이러스 출력

data = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if myMap[i][j] != 0:
      data.append((myMap[i][j], i, j)) 
      #  각 바이러스들의 번호와 좌표를 삽입
data.sort()
q = deque(data)

for _ in range(s):
  Qlen = len(q)
  for _ in range(Qlen):
    index, x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx and nx<n and 0<=ny and ny<n:
        if myMap[nx][ny] == 0:
          myMap[nx][ny] = myMap[x][y]
          q.append((myMap[nx][ny], nx, ny))
          # 빈곳이라면 전염시키고 힙에 삽입한다.

print(myMap[r-1][c-1])



