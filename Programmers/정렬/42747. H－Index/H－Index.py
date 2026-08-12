def solution(citations):
    n=len(citations)
    num= []
    for h in range(0,n+1):
        if sum(1 for x in citations if x>=h)>=h:
            num.append(h)
    return num[-1]