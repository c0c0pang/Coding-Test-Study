import sys
input = sys.stdin.readline

INF = int(1e9)

n,k = map(int,input().split())

arr = [int(input()) for _ in range(n)]

dp = [INF]*(100001)

dp[0] = 1

for i in arr:
    dp[i] = 1

for i in range(1,k+1):
    for j in arr:
        if i>=j:
            dp[i] = min(dp[i],dp[i-j]+1)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])