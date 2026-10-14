from collections import deque

def solution(prices):
    answer= [len(prices)-i-1 for i in range(len(prices))]
    stack = []
    for j,p in enumerate(prices):
        while stack and stack[-1][0]>p:
            s = stack.pop()
            answer[s[1]]=(j-s[1])
        stack.append((p,j))
    return answer 