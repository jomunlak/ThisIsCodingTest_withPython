# 숫자 카드 게임

n, m = map(int, input().split())
card = []
maxValue = -int(1e9)
for _ in range(n): maxValue = max(maxValue, sorted(list(map(int, input().split())))[0])

print(maxValue)