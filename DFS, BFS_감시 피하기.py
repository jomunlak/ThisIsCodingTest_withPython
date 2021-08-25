import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
data = [input().split() for _ in range(n)]

teachers = [] # 선생님의 좌표 리스트
space = [] # 빈 공간의 좌표 리스트 

for i in range(n):
  for j in range(n):
    if data[i][j] == 'T':
      teachers.append((i, j))
    elif data[i][j] == 'X':
      space.append((i, j))

def watch(x, y, dir): # 선생님의 위치와 방향에 맞춰 학생을 찾는 메서드
  global n
  if dir == 0: # 위로 찾기
    while x >= 0:
      if data[x][y] == 'O':
        break
      if data[x][y] == 'S':
        return True
      x -= 1
  elif dir == 1: # 아래
    while x < n:
      if data[x][y] == 'O':
        break
      if data[x][y] == 'S':
        return True        
      x += 1
  elif dir == 2: # 왼쪽
    while y >= 0:
      if data[x][y] == 'O':
        break
      if data[x][y] == 'S':
        return True        
      y -= 1
  elif dir ==3: # 오른쪽
    while y < n:
      if data[x][y] == 'O':
        break
      if data[x][y] == 'S':
        return True        
      y += 1
  return False # 학생을 찾을 수 없었다면 False 리턴


find = False
for i in combinations(space, 3):
  find = False
  for x, y in i:
    data[x][y] = 'O'
    # 장애물 설치
  
  for teacher in teachers:
    for dir in range(4):
      if watch(teacher[0], teacher[1], dir):
        find = True
        break # 학생을 한번이라도 찾았다면 숨기 실패

  if not find: # 모든 선생님이 학생을 찾지 못했다면 탐색 종료
    break

  for x, y in i:
    data[x][y] = 'X'
    # 설치한 장애물 지움  

if find:
  print("NO")
else:
  print("YES")