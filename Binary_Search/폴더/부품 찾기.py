import sys

N = int(sys.stdin.readline().rstrip())

N_array = list(map(int,sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())

M_array = list(map(int,sys.stdin.readline().rstrip().split()))

def BS(target,start,end):
    while start<=end:
        mid = (start+end)//2
        if N_array[mid] == target:
            return 'yes'
        if N_array[mid] > target:
            end = mid-1
            continue
        if N_array[mid] <target:
            start = mid+1
            continue
    return 'no'
N_array.sort()
M_array.sort()
for i in range(M):
    print(BS(M_array[i],0,N-1),end=' ')