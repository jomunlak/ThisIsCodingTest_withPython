
n = int(input())
arr = []
for _ in range(n):
  arr.append(input().split())
arr.sort(key = lambda x: x[1])
for i in arr:
  print(i[0], end = " ")