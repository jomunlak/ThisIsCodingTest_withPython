
s = input()
newstr = []
summ = 0

for i in s:
  print(ord(i))
  if ord(i) >= 65:
    newstr.append(i)
  else:
    summ += int(i)

newstr.sort()
for i in newstr:
  print(i, end = "")
print(summ)