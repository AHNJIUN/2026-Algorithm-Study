'''def solution(arr):
    q = [arr[0]]
    for i in range(len(arr)):
        if q[-1] != arr[i]:
            q.append(arr[i])
    return q'''

def solution(arr):
    return [n for i,n in enumerate(arr) if i==0 or arr[i-1] != n]