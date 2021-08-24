
n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse  = True)
for i in range(k):
  A[i] = B[i]
print(sum(A))