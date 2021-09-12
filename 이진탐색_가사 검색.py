# 이 코드는 프로그래머스에서 기본제공되는 코드를 이용해야 정상적으로 작동합니다.

import bisect
def solution(words, queries):
    answer = []
    sortedWords = [[] for _ in range(10001)]
    reversedWords = [[] for _ in range(10001)]
    for w in sorted(words, key = lambda x:(len(x), x)):
        bisect.insort(sortedWords[len(w)], w) # 단어를 길이별로 저장한 리스트
        bisect.insort(reversedWords[len(w)], w[::-1]) # 역순으로 저장한 리스트
    
    for q in queries:
        if q[0] != "?":
            # fro???를 찾는다면 froaaa ~ frozzz 사이에 있는 단어의 개수가 매칭되는 단어의 개수.
            left = bisect.bisect_left(sortedWords[len(q)], q.replace("?", "a"))
            right = bisect.bisect_right(sortedWords[len(q)], q.replace("?", "z"))
            answer.append(right - left)
        else:
            reversedQ = q[::-1]
            # ???do를 찾는다면 역순문자열 리스트에서 odaaa ~ odzzz 사이의 단어의 개수를 센다.
            left = bisect.bisect_left(reversedWords[len(q)], reversedQ.replace("?", "a"))
            right = bisect.bisect_right(reversedWords[len(q)], reversedQ.replace("?", "z"))
            answer.append(right - left)
        
    return answer