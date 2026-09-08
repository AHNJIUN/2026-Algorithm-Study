from collections import deque

def solution(prices):
    prices = deque(prices)
    lst = []
    while prices:
        t = 0
        p = prices.popleft()
        for c in prices:
            if p <= c:
                t += 1
            else : 
                t += 1
                break
        lst.append(t)        
    return lst