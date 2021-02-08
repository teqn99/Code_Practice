# 내 풀이
def solution(n):
    answer = 0    # 배터리 소모량
    while n >= 3:
        if n % 2 == 0:
            n = n // 2    # 순간이동
        elif n % 2 != 0:
            n -= 1    # K칸(1칸) 이동
            answer += 1

    if n == 3:
        answer += 2    # 3칸의 경우의 결과값
    elif n == 2 or n == 1:
        answer += 1    # 1칸 또는 2칸의 경우의 결과값

    return answer
    
    
    
# 다른 사람의 풀이
def solution(n):
    return bin(n).count('1')

# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# bin이 뭔지 
