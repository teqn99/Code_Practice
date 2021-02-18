# 나의 풀이
def solution(tr):
    answer = [0] * len(tr[-1])
    save = [0] * len(tr[-1])

    for i in range(len(tr)):
        if i == 0:
            for j in range(len(tr[i])):
                if save[j] < tr[i][j] + tr[i + 1][j]:
                    save[j] = tr[i][j] + tr[i + 1][j]
                save[j + 1] = tr[i][j] + tr[i + 1][j + 1]
            answer = save[:]
        else:
            for j in range(len(tr[i])):
                if save[j] < answer[j] + tr[i + 1][j]:
                    save[j] = answer[j] + tr[i + 1][j]
                save[j + 1] = answer[j] + tr[i + 1][j + 1]
            answer = save[:]
        if (i + 1) == (len(tr) - 1):
            break

    return max(answer)
# 다시 한 번 문제의 본질을 잊지 말자...(간단한 방법 놔두고 1시간을 고생했다...)



# 다른 사람의 풀이
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])
# 탐욕법(?)을 사용했다는 데, 다시 읽어보고 분석해서 내 것으로 만들기
