import sys
input = sys.stdin.readline


n,k = map(int,input().split())

arr = []

for i in range(n):
    n = int(input())
    if n>k:
        continue
    arr.append(n)


dp = [0]*(k+1)
dp[0] = 1
for i in arr:
    for j in range(1,k+1):
        if i>j:
            continue
        dp[j] = dp[j] + dp[j-i]
print(dp[k])