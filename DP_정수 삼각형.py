
n = int(input())
d = [[-1 for _ in range(n+1)] for _ in range(n+1)] 
for row in range(1, n+1):
  for col, val in enumerate(list(map(int, input().split())), start = 1):
    d[row][col] = val


for i in range(2, n+1):
  for j in range(1, n+1):
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]
print(max(d[n]))