n, m = map(int, input().split())
weights = list(map(int, input().split()))
check = 0

def func(n):
    if n == 1:
        return 1
    else:
        return n + func(n - 1)

result = func(n - 1)
for idx, val in enumerate(weights):
    for j in weights[idx + 1:]:
        if val == j:
            check += 1

print(result - check)
# 전체 경우의 수를 구하고, 겹치는 수가 있는 만큼 빼는 방법을 사용
# 시도해본 테스트 케이스들은 잘되었지만 문제가 있는 지는 더 알아봐야 한다.
# 그리디 문제를 푸는 방법을 다시 생각해보도록
