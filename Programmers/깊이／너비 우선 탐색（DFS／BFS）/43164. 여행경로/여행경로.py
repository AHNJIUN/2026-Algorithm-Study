def solution(tickets):
    remain = sorted(tickets, key=lambda ticket: ticket[1])
    def dfs(remain, path):
        if not remain:
            return path
        for i,t in enumerate(remain):
            if path[-1]==t[0]:
                result=dfs(remain[:i]+remain[i+1:], path + [t[1]])
                if result is not None:
                    return result
        return None
    return dfs(remain, ["ICN"])