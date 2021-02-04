# return 값을 그냥 b로 한 경우 -> 실패
# return 값을 b % 1234567로 한 경우 -> 성공
# --> 이유 분석해보기

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        a, b = 1, 2
        for i in range(1, n - 1):
            a, b = b, a + b        
    return b % 1234567
