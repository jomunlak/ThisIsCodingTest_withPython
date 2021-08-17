
# 이 코드는 프로그래머스에서 풀어야 작동합니다.

def getCorrect(u):
    stk = []
    for i in u:

        if i =="(":
            stk.append(i)
        else:
            if len(stk) == 0:
                return False
            else:
                stk.pop()

    return True

def getReverse(u):
    result = ""
    for i in u:
        if i == "(":
            result += ')'
        else:
            result += "("
    return result

def solution(p):

    answer = ''

    if p =="":
        return ""

    tmp = p[0]
    countA = 1 # 제일 첫번째 괄호의 개수
    countB = 0 # 첫번째 괄호의 반대 괄호의 개수
     # 가장 처음 만들어지는 균형잡힌 문자열을 구하는 코드
    for i in range(1, len(p)):        
        if tmp == p[i]:
            countA += 1
        else:
            countB += 1
        if countA == countB:
            # 두 종류의 괄호의 수가 같아지는 가장 짧은 문자열 구하기
            break

    u = p[:countA+countB] # 더이상 균형잡힌 문자열로 나뉘지 않는 균형잡힌 문자열
    v = p[countA+countB:]

    if getCorrect(u):
        answer += u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += getReverse(u[1:len(u)-1])

    return answer