from collections import deque
'''
def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = [0] * len(words)
    while q:
        x, answer = q.popleft()
        if x == target:
            return answer
        answer += 1
        for i in range(len(words)):
            if visited[i] != 1:
                cnt = 0
                for j in range(len(x)):
                    if x[j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append((words[i], answer))
                    visited[i] = 1
    return 0   
'''
def solution(begin, target, words):
    q = deque([(begin,0)])
    visited = set()
    while q:
        x,answer = q.popleft()
        if x == target:
            return answer
        for w in words:
            if w not in visited and sum(a!=b for a,b in zip(x,w))==1:
                q.append((w,answer+1))
                visited.add(w)
    return 0 