import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

array_A = list(map(int,sys.stdin.readline().rstrip().split()))

array_B = list(map(int,sys.stdin.readline().rstrip().split()))

array_A = sorted(array_A)
array_B = sorted(array_B,reverse=True)

for i in range(k):
    array_A[i],array_B[i] = array_B[i],array_A[i]
    
print(sum(array_A))