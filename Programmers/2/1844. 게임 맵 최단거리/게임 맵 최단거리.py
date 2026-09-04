from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0,0)])
    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr< n and 0<=nc< m and not visited[nr][nc] and maps[nr][nc]==1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))
    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1