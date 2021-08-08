
n, m = map(int, input().split())
# n : 공의 총 개수    m : 공의 최대 무게

balls = list(map(int, input().split()))
# 두 사람이 서로 다른 무게의 공을 고르는 경우의 수?
# 각 인덱스는 공의 번호.

result = 0
for i in range(len(balls)-1):
  for j in range(i+1,len(balls)):
    if balls[i] != balls[j]:
      result += 1

print(result)

