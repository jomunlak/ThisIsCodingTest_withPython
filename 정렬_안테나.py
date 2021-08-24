
n = int(input())
house= list(map(int, input().split()))
house.sort()
print(house[(n-1)//2]) # 원소의 중간값 구하기