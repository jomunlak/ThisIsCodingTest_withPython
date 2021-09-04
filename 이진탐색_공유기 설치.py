n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

start = 1 # 최소거리
end = houses[-1] - houses[0] # 최대 거리
result = 0

while start <= end:
  middle = (start + end) // 2 
  count = 1 # 설치한 공유기 개수. 제일 첫번째 집에 미리 한개를 설치했다.
  prev = houses[0] # 직전에 공유기를 설치한 위치.

  for i in range(1, n):
    if houses[i] >= prev + middle:
      count += 1
      prev = houses[i]

  if count >= c: # 설치한 공유기 개수가 충분하다면 최대값을 구하기 위해 거리를 늘려서 재실행
    result = middle
    start = middle +1
  else:
    end = middle - 1
print(result)