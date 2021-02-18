# 나의 풀이
def solution(land):
    lst = []

    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if k != j:
                    lst.append(land[i][j] + land[i - 1][k])
            land[i][j] = max(lst)
            lst = []

    return max(land[-1])
# 문제를 정확히 읽는 습관을 가지자...



# 다른 사람의 풀이
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
# 파이썬에서는 이런식으로 리스트의 합을 구할 수 있다는 점을 확실히 알아두기
