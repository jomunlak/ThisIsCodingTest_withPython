#1이 될 때까지

n, k = map(int, input().split())
result = 0
while n!= 1:
  if n<k:
    result += (n-1)
    break
  
  if n%k == 0:
    n = n//k
    result += 1
  else:
    result += n%k
    n -= n%k
print(result)