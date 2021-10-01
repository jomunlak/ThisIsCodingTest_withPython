# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse = True)
# 가장 큰 수와 그 다음으로 큰 수를 찾음
n1 = data[0]
n2 = data[1]

result = ((m//(k+1)) * ((k*n1)+n2)) + ((m%(k+1)) * n1)
print(result)