from collections import deque

def solution(maps):
    answer = 0
    dr = [-1,1,0,0]   # 상하좌우
    dc = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    q = deque([(0,0)])
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc]==0 and maps[nr][nc] != 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
    answer = dist[n-1][m-1] if dist[n-1][m-1] != 0 else -1

    return answer