import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = list(map(int,input().split()))

sum_num = 0
answer = 0
j = 0

for i in range(n):
    while sum_num <m and j<n:
        sum_num+=arr[j]
        j+=1
    if sum_num == m:
        answer+=1
    sum_num-=arr[i]
print(answer)