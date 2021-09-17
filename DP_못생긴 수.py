
n = int(input())
d = [0] * (n+1)
d[1] = 1 # 첫번째 못생긴 수는 1

i2, i3, i5 = 1, 1, 1
# 각각 못생긴수를 저장한 후 다음으로 제일 작은 못생긴수를 찾기위한 인덱스.
#  2, 3, 5 모두 따로 저장하기때문에 항상 제일 작은 수를 구할 수 있다.
next2, next3, next5 = 2, 3, 5

for i in range(2, n+1):
  d[i] = min(next2, next3, next5)
  if d[i] == next2:
    i2 += 1
    next2 = d[i2] * 2
  if d[i] == next3:
    i3 += 1
    next3 = d[i3] * 3
  if d[i] == next5:
    i5 += 1
    next5 = d[i5] * 5
    
print(d[n])
