def solution(progresses, speeds):
    from collections import deque
    answer = []
    days = deque()
    for p, s in zip(progresses, speeds):
        if ((100-p)/s) > ((100-p)//s):
            days.append(((100-p)//s)+1)
        else:
            days.append(((100-p)//s))
    while days:
        x = days.popleft()
        count = 1
        for _ in range(len(days)):
            y = days.popleft()
            if x >= y:
                count += 1
            else:
                days.appendleft(y)
                break
        answer.append(count)
    return answer