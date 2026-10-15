def solution(k, dungeons):
    lst = []
    def permutation(x, remain, path):
        state = False
        for i,d in enumerate(remain):
            need,use = d
            if x >= need:
                permutation(x-use, remain[:i]+remain[i+1:],path+[d])
                state = True
        if not state:
            lst.append(path)
    permutation(k, dungeons, [])
    return max([len(y) for y in lst])