# 이 코드는 프로그래머스에서 기본 제공되는 코드를 이용해야 정상작동합니다.

def solution(s):
    if len(s) <= 2:
        return len(s)
    
    answer = len(s)
    
    
    
    for step in range(1, len(s) // 2 +1):
        # 각 패턴의 숫자가 1 2 .. (문자열 길이의 절반) 일때의 압축된 문장의 길이를 계산한다.
        compressed = ""
        prev = s[0:step] # 첫 패턴
        count = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]: 
                count +=1
                # 문자열이 일치하면 카운트 증가
            else:
                compressed += str(count) + prev if count>= 2 else prev
                count = 1
                prev = s[j:j+step]
                # 문자열이 일치하지 않으면 압축된 문장에 넣기
        
        # 남은 문자열 넣기
        compressed += str(count) + prev if count>= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer
                