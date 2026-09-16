def solution(name):
    cnt = 0
    q,x =[], []
    for i,c in enumerate(name):
        dif = ord(c)-ord("A")
        if dif!=0:
            q.append(i)
            cnt += min(dif, 26 - dif)
    for k,j in enumerate(q):
        nxt = q[k+1] if k+1<len(q) else len(name)
        x.append(min(j+len(name)-(nxt-j), 2*(len(name)-nxt)+j))
    if x:
        cnt+=min(x)
    return cnt