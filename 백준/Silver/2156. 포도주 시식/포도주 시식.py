import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [(0,0)]*n
answer = 0
for _ in range(n):
    num = int(input())
    arr.append(num)

if n<=2:
    answer = sum(arr)
else:
    dp[0] = (arr[0],arr[0])
    dp[1] = (arr[1],arr[0]+arr[1])
    for i in range(2,n):
        n1,n2 = dp[i-2]
        n3,n4 = dp[i-1]
        dp[i] = (max(arr[i]+n1,arr[i]+n2),max(arr[i]+n3,n4))
        answer = max(dp[i][0],dp[i][1],answer)

print(answer)

      