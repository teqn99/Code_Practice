# 나의 풀이
from collections import deque

def solution(people, limit):
    answer = 0  # 배의 수
    people.sort()
    p = deque(people)
    
    while p:
        if len(p) >= 2:
            if p[0] + p[-1] <= limit:   # p[0] + p[-1] : 배에 탑승한 몸무게 합
                p.pop()
                p.popleft()
                answer += 1
            elif p[0] + p[-1] > limit:
                p.pop()
                answer += 1
        else:
            p.pop()
            answer += 1
    return answer
