
n, r, c = map(int, input().split())
counter = 0
answer = 0

def process(n, i, j, counter):
  global answer
  global r, c
  if n>1:
    halfN = 2**(n-1)
    if r < i + halfN and c < j + halfN:
      process(n-1, i, j, counter)
    elif r < i + halfN and c >= j + halfN:
      process(n-1, i, j + halfN, counter + halfN**2)
    elif r >= i + halfN and c < j + halfN:
      process(n-1, i + halfN, j , counter + 2*(halfN**2))    
    elif r >= i + halfN and c >= j + halfN:
      process(n-1, i + halfN, j + halfN, counter + 3*(halfN**2))   
  else:
    if r == i and c == j: answer = counter
    elif r == i and c == j+1: answer = counter+1
    elif r == i+1 and c == j: answer = counter+2
    elif r == i+1 and c == j+1: answer = counter+3
process(n, 0, 0, 0)

print(answer)