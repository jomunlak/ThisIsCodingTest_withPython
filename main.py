

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
  if target < x:
    break
  target += x

print(target)

# target과 같거나 작은 x에 대해 target + x 까지의 모든 수를 만들 수 있다.???????????????
