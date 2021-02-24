# 나의 풀이
def solution(n):
    a, b = 1, 2
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n - 2):
            a, b = b, a + b
        return b % 1000000007
      
# 생각보다 너무 쉬워서 놀란 문제
# 이 방법은 제대로 익힌 것 같다.(재귀안쓰는 방법)
