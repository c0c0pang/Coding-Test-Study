import sys

n = int(sys.stdin.readline())
dp = [1]*n
array = list(map(int,sys.stdin.readline().split()))
max_num = 0
box = [False]*n
for i in range(1,len(array)):
    for j in range(i-1,-1,-1):
        if(array[i]>array[j]):
            dp[i]=max(dp[i],dp[j]+1)
        else:
            print(j)
print(max(dp),box)