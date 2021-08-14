

numstr = input()
half = len(numstr)//2
s1 = numstr[0:half]
s2 = numstr[half:]

sum1, sum2 = 0, 0
for i in range(half):
  sum1 += int(s1[i])
  sum2 += int(s2[i])

if(sum1 == sum2):
  print("LUCKY")
else:
  print("READY")