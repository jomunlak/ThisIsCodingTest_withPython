
n = int(input())
mohumga = list(map(int, input().split()))
mohumga.sort()

i = 0       # 현재 확인하는 모험가의 인덱스
result = 0  # 전체 그룹의 수
count = 0   # 현재 그룹의 인원수

for i in range(n):

  count += 1 
  if mohumga[i] <= count:   # 정렬을 완료한 상태이기 때문에 현재의 공포도는 반드시 앞의 공포도보다 높거나 같다.
    count = 0               # 따라서 앞의 공포도를 확인할 필요 없이 현재의 공포도가 그룹의 수보다 같거나 작다면 그룹으로서 성립한다.
    result += 1                      



print(result)