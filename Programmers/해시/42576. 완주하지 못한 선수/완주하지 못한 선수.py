# def solution(participant, completion):
#     set_p, set_c = set([]), set([])
#     for p in participant:
#         n1=0
#         while (n1,p) in set_p:
#             n1 +=1
#         set_p.add((n1,p))
#     for c in completion:
#         n2=0
#         while (n2,c) in set_c:
#             n2 +=1
#         set_c.add((n2,c))
#     return list(set_p-set_c)[0][1]

def solution(participant, completion):
    d_p = {n:0 for n in participant}
    for p in participant:
        d_p[p] += 1
    for c in completion:
        d_p[c] -= 1
    return next(x for x in d_p if d_p[x]==1)