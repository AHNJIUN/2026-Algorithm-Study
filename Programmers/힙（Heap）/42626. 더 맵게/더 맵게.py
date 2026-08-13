import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville)>=2:
        if scoville[0]<K :
            h1=heapq.heappop(scoville)
            h2=heapq.heappop(scoville)
            heapq.heappush(scoville,h1+h2*2)
            cnt +=1
        else: break
    return cnt if scoville[0]>=K else -1