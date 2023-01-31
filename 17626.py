import sys
import math
n = int(sys.stdin.readline().rstrip())
dp = [1e9]*(50001)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,n+1):
    s=int(math.sqrt(i))
    p=int(math.pow(s,2))
    if i == p:
        dp[i] = 1
    else:
        for j in range(s,0,-1):
            p=int(math.pow(j,2))
            z= i-p
            dp[i] = min(dp[i],dp[p]+dp[z])

print(dp[n])