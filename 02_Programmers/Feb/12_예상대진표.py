# 나의 풀이
def solution(n, a, b):
    m = 1
    for i in range(n // 2):
        if (a < b and a % 2 != 0 and b % 2 == 0) or (a > b and a % 2 == 0 and b % 2 != 0):
            if bin(a) == bin(b - 1) or bin(a - 1) == bin(b):
                break

        if a == 1:
            a = 1
        elif a % 2 != 0:
            a = a // 2 + 1
        else:
            a = a // 2

        if b == 1:
            b = 1
        elif b % 2 != 0:
            b = b // 2 + 1
        else:
            b = b // 2

        m += 1

    return m
    
    
    
# 다른 사람의 풀이
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

# 이런 식으로 더 간단한 방법으로 고쳐서 연습하기
