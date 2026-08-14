from collections import deque

def solution(bridge_length, weight, truck_weights):
    lst = deque()
    truck_weights = deque(truck_weights)
    time = 0
    total = 0
    while truck_weights or lst:
        time += 1 
        if lst and time - lst[0][0] == bridge_length:
            total -= lst[0][1] 
            lst.popleft()
        if truck_weights and total + truck_weights[0] <= weight and len(lst)+1<=bridge_length :
            lst.append((time, truck_weights.popleft()))
            total += lst[-1][1]
    return time