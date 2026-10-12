def solution(name):
    total = sum(13-abs(ord(c)-ord("N")) for c in name)
    n=len(name)
    move = n-1 # 오른쪽으로 끝까지 이동하는 경우
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1
        right =i
        left = n - next_idx
        move=min(move, 2*right+left, 2*left+right)
    return total + move