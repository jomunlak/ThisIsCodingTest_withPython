

n = int(input())
student = []
for _ in range(n):
  student.append(input().split())

student.sort(key = lambda std: (-int(std[1]), int(std[2]), -int(std[3]), std[0] ))
for i in student:
  print(i[0])