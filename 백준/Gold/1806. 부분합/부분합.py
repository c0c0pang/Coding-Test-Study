import sys
input = sys.stdin.readline

n,s = map(int,input().split())

arr = list(map(int,input().split()))

sum_num = 0
j = 0
answer = 1e9
for i in range(n):
    while j<n and sum_num<s:
        sum_num+=arr[j]
        j+=1
    if sum_num>=s:
        answer = min(j-i,answer)
    sum_num-=arr[i]
if answer == 1e9:
    print(0)
else:
    print(answer)