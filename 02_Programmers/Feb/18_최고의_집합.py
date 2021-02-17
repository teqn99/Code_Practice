# 나의 풀이
def solution(n, s):
    if n > s:
        return [-1]

    answer = [s // n] * n
    plus = s - ((s // n) * n)

    for i in range(plus):
        answer[i] += 1

    return sorted(answer)
    
# 노가다보단 꼼수를 고민해보는 걸 연습하기
