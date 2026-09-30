import heapq

# def solution(operations):
#     q = []
#     for x in operations:
#         cmd, num = x.split()
#         if cmd=="I":
#             heapq.heappush(q, int(num))
#         elif q and cmd=="D":
#             if int(num)==-1:
#                 heapq.heappop(q)
#             elif int(num)==1:
#                 q.sort()
#                 q.pop()
#     q.sort()
#     return [q[-1], q[0]] if q else [0,0]

def solution(operations):
    q, max_q, min_q= {}, [], []
    for x in operations:
        cmd, num = x.split()
        if cmd == "I":
            heapq.heappush(max_q,-int(num))
            heapq.heappush(min_q,int(num))
            q[int(num)] = q.get(int(num),0) + 1
        elif (max_q or min_q) and cmd == "D":
            if int(num) == -1:
                min_value=heapq.heappop(min_q)
                q[min_value]-=1
            elif int(num) == 1:
                max_value=-heapq.heappop(max_q)
                q[max_value]-=1
        while min_q and q[min_q[0]]==0:
            heapq.heappop(min_q)
        while max_q and q[-max_q[0]]==0:
            heapq.heappop(max_q)
    return [-max_q[0],min_q[0]] if max_q else [0,0]