def solution(N, number):
    dp = [set() for _ in range(9)]
    for k in range(1,9):
        dp[k].add(int(str(N)*k))
        for i in range(1,k):
            for x in dp[k-i]:
                for y in dp[i]:
                    dp[k].add(x+y)
                    dp[k].add(x-y)
                    dp[k].add(x*y)
                    dp[k].add(x//y)
        dp[k]={v for v in dp[k] if v >0} 
        if number in dp[k]:
            return k
    return -1