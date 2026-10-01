def solution(word):
    dic = {"A":0, "E":1, "I":2, "O":3, "U":4}
    f = [1]
    for _ in range(4):
        f.append(f[-1]*5 +1)
    return sum(f[4-i]*dic[w] for i,w in enumerate(word))+len(word)