import sys

t = int(sys.stdin.readline().rstrip())
dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
numbox=[
    int(sys.stdin.readline().rstrip())
    for _ in range(t)
]
for i in range(6,max(numbox)+1):
        dp[i] = dp[i-1] + dp[i-5]

for i in numbox:
    print(dp[i])