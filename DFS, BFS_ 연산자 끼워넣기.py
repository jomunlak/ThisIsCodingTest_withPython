
n = int(input())
nums = list(map(int, input().split()))
opsNum = list(map(int, input().split()))
ops = []
n = len(nums)
maxRes = -999999999
minRes = 999999999

for i in range(len(opsNum)):
  for j in range(opsNum[i]):
    ops.append([i, False])
    # 연산자 번호와 사용여부를 저장함

def calc(a, b, op):
  if op == 0:
    return a + b
  elif op == 1:
    return a- b
  elif op ==2:
    return a * b
  else:
    if a < 0:
      tmp = -a // b
      return -tmp
    else:
      return a//b

  
# dfs와 bfs를 이용한다는 것은 재귀를 잘 이용한다는 의미가 포함되어있는것 같다...
def dfs(res, count):
  global minRes
  global maxRes
  if count == n:
    # 연산자를 모두 삽입했을 경우
    maxRes = max(res, maxRes)
    minRes = min(res, minRes)
    return

  # 가지고있는 모든 연산자에 대해 사용중이지 않은 연산자를 이용해 계산한 후 
  for i in range(len(ops)):
    if not ops[i][1]:
      
      tmp = calc(res, nums[count], ops[i][0])
      ops[i][1] = True
      count += 1
      dfs(tmp, count)
      ops[i][1] = False
      count -= 1
  
dfs(nums[0], 1)
print(maxRes)
print(minRes)