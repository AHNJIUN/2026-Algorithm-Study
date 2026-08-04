from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        days.append(ceil((100-progresses[i])/speeds[i]))
    while days:
        deploy_days=days.popleft()
        deploy_count=1
        while days and days[0] <= deploy_days:
            days.popleft()
            deploy_count+=1
        answer.append(deploy_count)
    return answer