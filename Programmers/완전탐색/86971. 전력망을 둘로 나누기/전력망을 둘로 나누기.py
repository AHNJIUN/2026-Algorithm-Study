def solution(n, wires):
    lst=[]
    def graph(start,lst):
        for node in lst:
            if start in node:
                a,b = node
                end=b if start==a else a
                if end not in g:
                    g.append(end)
                    graph(end,lst)
    for i in range(len(wires)):
        g=[1]
        remain = wires[:i] + wires[i+1:]
        graph(g[0],remain)
        lst.append(abs(n-2*len(g)))
    return min(lst)