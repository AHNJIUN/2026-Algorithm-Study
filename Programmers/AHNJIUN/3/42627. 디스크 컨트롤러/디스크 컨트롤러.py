import heapq

def solution(jobs):
    wait = []
    time=0
    total = 0
    jobs.sort()
    idx = 0
    for _ in range(len(jobs)):
        if not wait and idx < len(jobs):
            time = max(time, jobs[idx][0])
        while idx < len(jobs) and jobs[idx][0] <= time:
            s,l = jobs[idx]
            heapq.heappush(wait,(l,s))
            idx += 1
        x,y = heapq.heappop(wait)
        time+= x
        total += time - y
    return total//len(jobs)