#최적화 되지 않은 코드

def solution(food_times, k):
    
    target = 0
    # 남은 음식들 n개 중에 가장 작은 음식의 개수가  m이라고 가정했을때
    # k >= n * m 이라면 남은 음식 [0 ~ n-1]에 대해 m 씩 빼고, k - n*m이 가능하다.   

    #내일 올라가서 생각하자
    for _ in range(k):
        
        food_times[target] -= 1
        target = getNextTarget(food_times, target)
        
        if target == -1:
            return -1
        
    answer = target + 1
    return answer

def getNextTarget(food_times, targetNow):
    
    nextTarget = targetNow
    for _ in range(len(food_times)):
        nextTarget = (nextTarget + 1) % len(food_times) #원형 식탁의 다음 음식을 고르는 식
        
        if food_times[nextTarget] != 0:
            return nextTarget

    return -1