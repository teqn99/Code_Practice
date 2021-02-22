# 나의 풀이
def solution(dirs):
    x, y = 0, 0
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    road = []

    for idx, val in enumerate(list(dirs)):
        if val == 'U':
            dx, dy = d['U']
            if y < 5:
                nx, ny = x + dx, y + dy
            if [x, y, nx, ny] not in road and y != ny:
                road.append([x, y, nx, ny])
                road.append([nx, ny, x, y])
                x, y = nx, ny
            else:
                x, y = nx, ny
        elif val == 'D':
            dx, dy = d['D']
            if y > -5:
                nx, ny = x + dx, y + dy
            if [x, y, nx, ny] not in road and y != ny:
                road.append([x, y, nx, ny])
                road.append([nx, ny, x, y])
                x, y = nx, ny
            else:
                x, y = nx, ny 
        elif val == 'R':
            dx, dy = d['R']
            if x < 5:
                nx, ny = x + dx, y + dy
            if [x, y, nx, ny] not in road and x != nx:
                road.append([x, y, nx, ny])
                road.append([nx, ny, x, y])
                x, y = nx, ny
            else:
                x, y = nx, ny
        if val == 'L':
            dx, dy = d['L']
            if x > -5:
                nx, ny = x + dx, y + dy
            if [x, y, nx, ny] not in road and x != nx:
                road.append([x, y, nx, ny])
                road.append([nx, ny, x, y])
                x, y = nx, ny
            else:
                x, y = nx, ny

    return len(road) // 2
    
# 반대로 가도 지나왔던 길임을 생각해봐야 했던 문제
# 앞으로는 문제를 보면서 먼저 그림을 그려보고 아이디어를 적어보는 습관을 기르도록 하자
