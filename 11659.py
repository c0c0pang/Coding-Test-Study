import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

array = list(map(int,sys.stdin.readline().rstrip().split()))
s=[0]*(n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + array[i-1]
for i in range(m):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    print(abs(s[n2]-s[n1-1]))