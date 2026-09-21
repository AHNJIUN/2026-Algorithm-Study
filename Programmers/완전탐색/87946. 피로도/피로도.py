def solution(k, dungeons):
    q,cnt = [], []
    def cnt_dungeon(k, remain, path):
        for i, lst in enumerate(remain):
            a,b = lst
            if remain and k-a >=0:
                cnt_dungeon(k-b, remain[:i]+remain[i+1:], path + [remain[i]])
        cnt.append(len(path))
    cnt_dungeon(k, dungeons, q)
    return max(cnt)