
targetStr = input()
editStr = input()

row = len(editStr)
col = len(targetStr)

# d[i][j] : editStr[i]를 targetStr[j]로 만들기 위해 필요한 최소 편집횟수
d = [[0] * (col+1) for _ in range(row + 1)]
for i in range(col+1): d[0][i] = i
for i in range(row+1): d[i][0] = i

for i in range(1, row+1):
  for j in range(1, col+1):
    if editStr[i - 1] == targetStr[j -1]:
      d[i][j] = d[i-1][j-1] 
    else: # 비교하는 문자가 다르다면 왼쪽(삽입), 위(삭제), 왼쪽 대각선 위(교체) 중 가장작은 하나를 선택해 편집횟수 1을 더한다
      d[i][j] = 1 + min(d[i-1][j-1], d[i][j-1], d[i-1][j])

print(d[row][col])

