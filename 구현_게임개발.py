

n, m = map(int, input().split())

chr_x, chr_y, chr_dir = map(int, input().split())

mapList = []
for i in range(n):
  mapList.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  # 북, 동, 남, 서

result = 0

while True:
  if mapList[chr_x][chr_y] == 0:
    mapList[chr_x][chr_y] = 2
    print("mapList["+str(chr_x)+"]["+str(chr_y)+"] 탐색")
    result += 1
  elif mapList[chr_x][chr_y] == 1: #뒤로 돌아 온 곳이 바다라면 종료
    break
  
  for i in range(4):
    chr_dir = (chr_dir +3) %4
    if mapList[chr_x + dx[chr_dir]][chr_y + dy[chr_dir]] == 0:
      chr_x += dx[chr_dir]
      chr_y += dy[chr_dir] # 왼쪽이 비어있으면 그쪽으로 이동
      break
    else: 
      if i == 3: # 모든 방향이 갈곳이 아닐때
        chr_x += dx[(chr_dir + 2) % 4]
        chr_y += dy[(chr_dir + 2) % 4]

print(result)