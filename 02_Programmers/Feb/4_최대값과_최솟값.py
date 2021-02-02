def solution(s):
    ans = [int(i) for i in list(s.split(' '))]
    mina, maxa = min(ans), max(ans)  

    return f'{mina} {maxa}'
    
    
    
# 다른사람의 풀이
# -> map 함수 사용 익히기
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
