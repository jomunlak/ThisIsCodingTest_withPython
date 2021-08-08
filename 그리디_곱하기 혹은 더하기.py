
s = input()
n = []
for i in range(len(s)):
  n.append(int(s[i]))

result = 0

for i in n:
  # 현재 수를 더했을때 더 크면 더하고, 곱했을때 크면 곱한다.
  # --> 0 혹은 1일경우 더해지고 이외에는 곱해진다.
  # 이 방법으로 0에 숫자를 곱해서 생기는 문제를 막을 수 있다.
  if i + result > i * result:
    result += i
  else:
    result *= i

print(result)

