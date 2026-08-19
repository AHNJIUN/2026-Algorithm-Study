from collections import deque

def solution(priorities, location):
    s = deque([(p,i) for i, p in enumerate(priorities)])
    l = []
    while s:
        c = s.popleft()
        if any(x[0] >c[0] for x in s) :
            s.append(c)
        else :
            l.append(c)
    for idx, (p,i) in enumerate(l):
        if i == location:
            return idx + 1