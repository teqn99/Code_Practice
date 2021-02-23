# 나의 풀이
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    print(costs)
    routes = set([costs[0][0]]) # 집합
    print(routes)
    
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                del costs[i]
                print(routes)
                break
    return ans

# kruskal 알고리즘에 대해 개념을 잡지 못해 많이 해메었다.
# 구글링해서 참조해서 푼 문제
# 탐욕, 탐색 알고리즘 등 공부해볼 것
