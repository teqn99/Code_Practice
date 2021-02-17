# 나의 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 남은 트럭들이 가야하는 거리
    time = 0  # 소요시간
    bridge_weight = 0  # 다리 위의 무게

    while len(bridge) != 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left = truck_weights.popleft()
                bridge_weight += left
                bridge.append(left)
            else:
                bridge.append(0)

    return time
    
# bridge = deque([0] * bridge_length) -> 이 부분 사용하는거 손에 익혀두기
# 거리나 그런 계산에 유용하게 쓸 수 있는 것 같다. (deque부분은 필수가 아니라 유동적으로 사용하는 거고)
