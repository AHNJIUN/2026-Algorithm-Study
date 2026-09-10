'''
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    lst_abc = [a,b,c]
    lst = [0, 0, 0]
    answer = []
    for i in range(len(answers)):
        for x in range(len(lst_abc)):
            k = lst_abc[x]
            if k[i%len(k)] == answers[i]:
                lst[x] += 1
    m = max(lst)
    for j in range(len(lst)):
        if lst[j] == m:
            answer.append(j+1)            
    return answer

def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    lst_abc = [a,b,c]
    lst = [0]*len(lst_abc)
    for i,x in enumerate(lst_abc):
        for j,y in enumerate(answers):
            if x[j%len(x)] == y:
                lst[i] += 1
    m = max(lst)
    return [k+1 for k in range(len(lst)) if lst[k] == m]
'''
def solution(answers):
    lst_abc = ([1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5])
    lst=[sum(1 for j,y in enumerate(answers) if x[j%len(x)]==y) for x in lst_abc]
    m = max(lst)
    return [k+1 for k,z in enumerate(lst) if z == m]