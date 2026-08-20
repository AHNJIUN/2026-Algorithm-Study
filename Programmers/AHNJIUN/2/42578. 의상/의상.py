from collections import Counter

def solution(clothes):
    s = 1
    c = Counter(kind for name, kind in clothes)
    for i in c.values():
        s *= (i+1)
    return s-1