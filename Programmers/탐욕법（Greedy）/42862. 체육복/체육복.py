'''def solution(n, lost, reserve):
    x,y = set(lost),set(reserve)
    for a in x&y:
        x.remove(a)
        y.remove(a)
    for b in sorted(x):
        if b-1 in y:
            x.remove(b)
            y.remove(b-1)
        elif b+1 in y:
            x.remove(b)
            y.remove(b+1)
    return n-len(x)'''

def solution(n, lost, reserve):
    x,y = set(lost)-set(reserve), set(reserve)-set(lost)
    for a in sorted(x):
        if a-1 in y:
            x.remove(a)
            y.remove(a-1)
        elif a+1 in y:
            x.remove(a)
            y.remove(a+1)
    return n-len(x)