def solution(number, k):
    len_x = len(number)-k
    x=[]
    for c in number:
        while x and c>x[-1] and k>0:
            x.pop()
            k-=1
        x.append(c)
    return "".join(x[:len_x])