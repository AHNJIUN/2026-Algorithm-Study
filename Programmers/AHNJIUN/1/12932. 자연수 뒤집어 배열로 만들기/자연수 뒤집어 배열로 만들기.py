def solution(n):
    return [int(str(n)[-1-i]) for i in range(len(str(n)))]