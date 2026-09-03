def solution(triangle):
    dp =[[0]*len(row) for row in triangle]
    dp[0][0]=triangle[0][0]
    for n in range(1, len(triangle)):
        for i in range(len(triangle[n])):
            if i==0:
                dp[n][i] = dp[n-1][i]+triangle[n][i]
            elif i==len(triangle[n])-1:
                dp[n][i] = dp[n-1][i-1]+triangle[n][i]
            else:
                dp[n][i] = max(dp[n-1][i-1], dp[n-1][i]) + triangle[n][i]
    return max(dp[n][i] for i in range(len(triangle[n])))
