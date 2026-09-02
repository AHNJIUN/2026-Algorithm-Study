def solution(number, k):
    lst = []
    n = len(number)-k
    for c in number:
        while k>0 and lst and c > lst[-1]:
            k-=1
            lst.pop()
        lst.append(c)
    return "".join(lst[:n])