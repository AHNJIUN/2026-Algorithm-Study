def solution(n, wires):
    result= []
    for i in range(len(wires)):
        lst = wires[:i]+wires[i+1:]
        graph = [1]
        def dfs(cur):
            for node in lst:
                a,b = node
                nxt=b if a==cur else a
                if cur in node and nxt not in graph:
                    graph.append(nxt)
                    dfs(nxt)
        dfs(1)
        result.append(abs(n-2*len(graph)))
    return min(result)