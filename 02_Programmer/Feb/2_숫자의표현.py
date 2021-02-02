def solution(n):
    m, answer, ans = n // 2, 1, 0    # answer: n 자기자신도 결과에 포함

    for i in range(1, m + 1):
        ans = 0
        for j in range(i, m + 1):
            ans += j
            if ans == n:
                answer += 1
                break
            if ans > n:
                break

    if n % 2 != 0:
        # n이 홀수인 경우, 반으로 나눈값 + 그값보다 하나 큰 값을 하면 결과에 포함
        answer += 1    

    return answer
