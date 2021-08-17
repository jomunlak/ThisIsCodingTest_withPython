import itertools

n = int(input())
nums = list(map(int, input().split()))
opsIndex = list(map(int, input().split()))
opsLen = sum(opsIndex)
ops = []
for i in range(len(opsIndex)):
  for j in range(opsIndex[i]):
    ops.append(i)
# ops : 쓸 수 있는 연산자들의 리스트
opsPm = list(itertools.product(ops, repeat = (3)))
# 0 : +   1:-   2:*    3:/

minRes = 999999999
maxRes = -999999999

for i in opsPm:
  result = nums[0]
  for j in range(opsLen):
    if i[j] == 0:
      result += nums[j+1]
    elif i[j] == 1:
      result -= nums[j+1]
    elif i[j] == 2:
      result *= nums[j+1]
    else:
      if result < 0:
        result = -(-result//nums[j+1])
      else:
        result //= nums[j+1]
  minRes = min(result, minRes)
  maxRes = max(result, maxRes)

print(maxRes)
print(minRes)


