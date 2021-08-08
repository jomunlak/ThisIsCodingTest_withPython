import itertools

#그리디 알고리즘을 사용하지 않는 버전.

n = int(input())
numList = list(map(int, input().split()))

s = set([]) # 만들 수 있는 수의 집합을 만든다.
sum = 0

# i = 1일때 만들 수 있는 수들의 집합 | i = 2 일때 만들수 있는 수들의 집합 | .....| i = len(n)일때 만들 수 있는 집합

for i in range(1, n+1):
 
  pmt = list(itertools.permutations(numList,i))
  # i 
  for j in range(len(pmt)):
    for k in range(i):
      sum += pmt[j][k]
    s.add(sum)
    sum = 0

for i in range(1,1000):
  if i not in s:
    print(i)
    break





