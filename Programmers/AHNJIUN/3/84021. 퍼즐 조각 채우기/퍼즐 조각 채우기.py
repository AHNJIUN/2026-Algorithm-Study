def solution(game_board, table):
    max_rc= len(game_board[0])
    dr = [-1,1,0,0]   # 상하좌우
    dc = [0,0,-1,1]
    g,t = 0,1
    pieces = [[],[]]
    cnt = 0
    def puzzle(board,piece):
        visited = []
        def dfs(r,c,board,piece):
            lst.append([r,c])
            for d in range(4):
                nr,nc = r + dr[d], c + dc[d]
                if [nr,nc] not in visited and 0<=nr<max_rc and 0<=nc<max_rc and board[nr][nc]==piece:
                    visited.append([nr,nc])
                    dfs(nr,nc,board, piece)
        for i in range(max_rc):
            for j in range(max_rc):
                if [i,j] not in visited and board[i][j] == piece:
                    visited.append([i,j])
                    lst = []
                    dfs(i,j,board,piece)
                    normalize(lst)
                    x = lst
                    rotations = []
                    for _ in range(4):
                        x=rotate(x)
                        normalize(x)
                        rotations.append(x)
                    pieces[piece].append(rotations) if piece==t else pieces[piece].append(lst)                        
    def normalize(lst):
        min_r, min_c = lst[0][0], lst[0][1]
        for r,c in lst:
            if r < min_r:
                min_r = r
            if c < min_c:
                min_c = c
        for i in range(len(lst)):
            lst[i][0] -= min_r
            lst[i][1] -= min_c
        lst.sort()
    def rotate(lst):
        rotate_lst = []
        for r,c in lst:
            rotate_lst.append([-c,r])
        return rotate_lst
    puzzle(game_board,g)
    puzzle(table,t)
    for blank in pieces[0]:
        for p in pieces[1]:
            if blank in p:
                cnt += len(blank)
                pieces[1].remove(p)
                break
    return cnt