import heapq

n = int(input())
d = [0, 1] 
idx = 2
for i in range(1, 50):
  for j in range(1, 50):
    for k in range(1, 50):
      heapq.heappush(d, (i**2) * (j**3) * (k**5))
print(d)



