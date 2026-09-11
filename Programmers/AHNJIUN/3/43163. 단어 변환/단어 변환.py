from collections import deque

def solution(begin, target, words):
    q = deque([(begin,0)])
    visited = [0]*len(words)
    while q:
        x,answer = q.popleft()
        if x == target:
            return answer
        answer += 1
        for i in range(len(words)):
            if visited[i]!=1:
                cnt = 0
                for j in range(len(x)):
                    if x[j]!=words[i][j]:
                        cnt+=1
                if cnt==1:
                    q.append((words[i],answer))
                    visited[i] = 1
    return 0