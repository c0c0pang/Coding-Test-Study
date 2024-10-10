import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n)]

fw,fv = map(int,input().split())

for i in range(1,k+1):
    if i<fw:
        continue
    dp[0][i] = fv

for i in range(1,n):
    w,v = map(int,input().split())

    for j in range(1,k+1):
        if w>j:
            dp[i][j] = dp[i-1][j]
            continue
        
        dp[i][j] = max(dp[i-1][j],v+dp[i-1][j-w])
print(dp[-1][-1])