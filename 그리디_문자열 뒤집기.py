# 문자열 뒤집기

# idea) 0혹은 1로만 이루어져있는 문자열, 0의 조각과 1의 조각의 개수를 세서 더 작은쪽의 개수가??

s = input()

tmp = s[0]
count0 = 0
count1 = 0
if tmp == '1':
  count1 += 1
else:
  count0 += 1

for i in range(1,len(s)):
  if tmp == s[i]:
    continue
  else:
    tmp = s[i]
    if tmp == '1':
     count1 += 1
    else:
     count0 += 1

print(min(count0, count1))

