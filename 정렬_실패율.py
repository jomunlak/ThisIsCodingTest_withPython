# 이 문제는 프로그래머스에서 기본제공되는 코드를 이용하여 풀어야 작동합니다.

def solution(N, stages):
    
    answer = []
    tempResult = []
    fail = 0
    
    # 각 단계에서 막힌 사람들의 수
    stop = [0] *(N+2)
    for i in stages:
        stop[i] += 1    
        
    # 현재 단계까지 도착한 사람의 수(전체인원이 1단계 도착)
    arrive = len(stages)
    
    for i in range(1,N+1):
        
        if arrive == 0:
            fail = 0   
            # 현재 단계에 도착한 사람이 없다면 실패율 0
        else:
            fail = stop[i] / arrive
            arrive -= stop[i]
            # 다음 단계에 도착한 사람 = 전단계에 도착한 사람 - 전단계에서 막힌 사람
        tempResult.append((i, fail))
    
    tempResult.sort(key = lambda x:x[1], reverse =True)
    answer = [i[0] for i in tempResult]
            
    return answer