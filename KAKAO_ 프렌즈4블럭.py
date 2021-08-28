# 이 코드는 프로그래머스에서 기본제공되는 코드를 이용해야지만 정상작동합니다.

def drop(m, n, board):
    for j in range(0, n):
        for i in range(m-1, 0, -1):
            if board[i][j] == '-':
                for k in range(i - 1, -1, -1):
                    if board[k][j] != '-':
                        board[i][j], board[k][j] = board[k][j], board[i][j]
                        break



def solution(m, n, board):

    answer = 0
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]
    # 특정 인덱스의 주변 4블럭의 위치
    delete = set() 
    # 삭제할 인덱스들의 집합
    
    for i in range(m):
        board[i] = list(board[i])
        # 문자열을 원소를 바꾸기 용이하도록 리스트로 바꾼다.
    while True:
        for r in range(m -1):
            for c in range(n-1):
                tmp = board[r][c] 
                if tmp == '-': 
                    continue
                    # 현재 문자가 공백이라면 무시
                    
                square = True
                for i in range(4):
                    if board[r + dr[i]][c + dc[i]] != tmp:
                        square = False # 4블럭중 하나라도 다르다면 삭제하지않는다.
                        break
                if square:
                    for i in range(4):
                        delete.add((r + dr[i], c + dc[i]))
                        # 삭제할 사각형을 찾았다면 삭제할 인덱스들의 집합에 사각형을 추가

        if len(delete) == 0:
            break
            # 아무것도 삭제할것이 없다면 종료
        
        answer += len(delete)

        while delete:
            x, y = delete.pop()
            board[x][y] = '-'        
            # 집합에있는 모든 좌표들에대해 공백을 나타내는 문자로 바꿈
        drop(m, n, board)
        # 삭제가 끝난 후 원소들 떨어트리기
        

    return answer