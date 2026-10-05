def solution(n, costs):
    lst = sorted(costs, key=lambda x:x[2])
    graph, total = [], 0
    def dfs(start, goal, visited):
        for g in graph:
            if start not in g:
                continue
            nxt = g[1] if g[0]==start else g[0]
            if nxt == goal:
                return True
            elif nxt not in visited:
                visited.append(nxt)
                if dfs(nxt, goal, visited):
                    return True
        return False
    for c in lst:
        a, b, cost = c
        if not dfs(a,b,[a]):
            graph.append([a,b])
            total += cost
        if len(graph) == n-1:
            return total