import sys
t = int(sys.stdin.readline().rstrip())
dp = [0]*12
array = [
    int(sys.stdin.readline().rstrip())
    for _ in range(t)
]
maxnum = max(array)
dp[1]=1
dp[2]=2
dp[3]=4
for j in range(4,maxnum+1):
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
        
for i in array:
    print(dp[i])