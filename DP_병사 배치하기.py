
n = int(input())
sordier = list(map(int, input().split()))
d = [1] * n
# d[i] : sordier[i]를 마지막 원소로 가지는 부분 순열의 최대길이
for i in range(1, n):
  for j in range(0, i):
    # 0이상 i 미만의 모든 j에대해 감소하는 조건이 충족된다면 
    if sordier[j] > sordier[i]:
      d[i] = max(d[i], d[j] + 1)

print(n - max(d))


# LIS(Longest Increasing Subsequence) 최장 증가하는 부분순열 문제를 
# "증가하는"이 아닌 "감소하는" 순열로 바꾸는것으로 간단하게 풀 수 있는 문제.