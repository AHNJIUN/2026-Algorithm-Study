def solution(n, computers):
    visited = [False] * n
    cnt=0
    def relation(i):
        for j in range(n):
            visited[i]=True
            if not visited[j] and computers[i][j]:
                relation(j)
    for c in range(n):
        if not visited[c]:
            relation(c)
            cnt+=1
    return cnt