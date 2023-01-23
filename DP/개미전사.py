import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0]*n
dp[0]=array[0]
dp[1]=max(array[0],array[1])
for i in range(2,n):
    dp[i] = dp[i-2]+array[i] 
    dp[i] = max(dp[i],dp[i-1])
   
print(dp[n-1])