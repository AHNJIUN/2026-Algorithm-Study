'''def solution(n, times):
    lo,hi = min(times),max(times)*n
    def ok(mid):
        k=0
        for t in times:
            k+=mid//t
        return k>=n
    while lo<hi:
        mid = (lo+hi)//2
        if ok(mid):
            hi = mid
        else :
            lo = mid+1
    return lo'''

def solution(n, times):
    lo,hi = min(times),max(times)*n
    while lo<hi:
        mid = (lo+hi)//2 
        if sum(mid//t for t in times)>=n:
            hi = mid
        else :
            lo = mid+1
    return lo