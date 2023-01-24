import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
array = []
dp = [10001]*(m+1)
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))
    if array[i]<=m:
        dp[array[i]]=1
    
for i in range(1, m+1):
    for j in array:
        if i-j>=0:
            dp[i] = min(dp[i-j]+1,dp[i])
if dp[m]==10001:
    print(-1)
else:
    print(dp)
