'''
from collections import deque

def solution(prices):
  prices = deque(prices)
  lst = []
  while prices:
      t = 0
      p = prices.popleft()
      for c in prices:
          t += 1
          if p > c:
              break
      lst.append(t)
  return lst
'''
from collections import deque

def solution(prices):
    stack = deque([])
    answer = [0]*len(prices)
    for j,price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            answer[stack[-1]]= j - stack[-1]
            stack.pop()
        stack.append(j)
    for i in stack:
        answer[i] = len(prices)-i-1
    return answer