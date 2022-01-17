def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] *bridge_length
    time = 0
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                bridge.append(0)
    return time
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))