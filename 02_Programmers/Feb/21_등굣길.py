# 나의 풀이 1
def solution(m, n, puddles):
    route= [[0]*(m+1) for i in range(n+1)]
    route[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:
                route[i][j] = 0

            else:
                route[i][j] = route[i-1][j] + route[i][j-1]

    answer = route[n][m]
    return answer % 1000000007
    
# 나의 풀이 2
def solution(m, n, puddles):
    route=[[0] * (m + 1) for _ in range(n + 1)]    
    route[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                route[i][j] = 0 
            else:
                route[i][j] = route[i - 1][j] + route[i][j - 1]
                
    return route[-1][-1] % 100000007
    
# 나의 풀이 3
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _i in range(n + 1)]
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i, j] != [1, 1] and [i, j] not in puddles:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
    print(dp)
    return dp[n][m] % 1000000007
    
# 1, 2 는 리턴값 구조만 다른데 1은 되고 2는 안되는 이유 생각해보기
# 3은 따지고 보면 같은 구조인데 안되는 이유 생각해보기



# 다른 사람의 풀이
def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007
    
# 딕셔너리를 이용하는 방법도 다시 보자
