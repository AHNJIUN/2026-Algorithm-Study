def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            w,h=sizes[i][0], sizes[i][1]
            sizes[i][0],sizes[i][1] = h,w
    return max(w for w,h in sizes)*max(h for w,h in sizes)