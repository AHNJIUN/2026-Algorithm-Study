from collections import deque

'''def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    cnt = 0
    for a,b in results:
        win[a].append(b)
        lose[b].append(a)
    for i in range(1,n+1):
        visited= [False]*(n+1)
        q = deque([i])
        while q:
            cur = q.popleft()
            for x in (win, lose):
                for nxt in win[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
        q = deque([i])
        while q:
            cur = q.popleft()
            for nxt in lose[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        if sum(visited) == n-1:
            cnt+=1
    return cnt'''

def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    for a,b in results:
        win[a].append(b)
        lose[b].append(a)
    def is_rank(i):    
        visited= [False]*(n+1)
        for graph in (win, lose):
            q = deque([i])
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
        return sum(visited)==(n-1)
    return sum(1 for i in range(1,n+1) if is_rank(i))