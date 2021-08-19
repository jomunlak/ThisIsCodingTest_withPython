

n, m = map(int, input().split())

# 초기 연구소 
Lab = []
for i in range(n):
  Lab.append(list(map(int, input().split())))

# 벽을 세운 후의 연구소
tmp = [[0 for _ in range(m)] for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 기둥이 세워지는 모든 경우의 수를 구하여 
# 각 경우의 수마다 안전 영역의 크기를 구한다. 영역의 크기중 가장 큰 것을 결과로 반환한다.

# 안전 영역의 개수를 세는 메서드
def safeCount():
  count = 0
  for i in range(len(tmp)):
    for j in tmp[i]:
      if j == 0:
        count += 1
  return count

# (x, y) 지역에 바이러스가 발견되었을 경우 주변에 퍼트리는 메서드
def virus(x, y):
  tmp[x][y] = 2

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= nx and nx < n and 0<= ny and ny < m:
      if tmp[nx][ny] == 0:
        virus(nx, ny)

result = 0

def dfs(count):
  global result 

  if count == 3:
    for i in range(n):
      for j in range(m):
        tmp[i][j] = Lab[i][j]
    for i in range(n):
      for j in range(m):
        if tmp[i][j] == 2:
          virus(i, j)
    result = max(result, safeCount())
    return

  for i in range(n):
    for j in range(m):
      if Lab[i][j] == 0:
        Lab[i][j] = 1
        count += 1
        dfs(count)
        Lab[i][j] = 0
        count -= 1

dfs(0)
print(result)