# def solution(genres, plays):
#     total = {x:0 for x in genres}
#     lst = [[] for _ in range(len(total))]
#     best = []
#     for i in range(len(genres)):
#         total[genres[i]] += plays[i]
#     total = sorted(total, key=total.get, reverse=True)
#     for j in range(len(total)):
#         lst[j] = sorted([(play,k) for k,play in enumerate(plays) if total[j]==genres[k]], key=lambda x:(-x[0],x[1]))
#     for k in range(len(lst)):
#         for play, idx in lst[k][:2]:
#             best.append(idx)
#     return best

def solution(genres, plays):
    total = {x:0 for x in genres}
    lst = []
    best = []
    for genre, play in zip(genres,plays):
        total[genre] += play
    total = sorted(total, key=total.get, reverse=True)
    lst = [sorted([(play,k) for k,play in enumerate(plays) if g==genres[k]], key=lambda x:(-x[0],x[1])) for g in total]
    return [idx for k in lst for _, idx in k[:2]] 