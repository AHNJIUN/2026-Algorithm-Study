from collections import deque

def solution(people, limit):
    p = deque(sorted(people))
    cnt = len(p)
    while len(p)>1:
        if p[-1]+p[0]<=limit:
            p.pop()
            p.popleft()
            cnt-=1
        else:
            p.pop()
    return cnt