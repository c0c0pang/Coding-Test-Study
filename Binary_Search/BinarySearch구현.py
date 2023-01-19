import sys

N,S = map(int,sys.stdin.readline().rstrip().split())

array = list(map(int,sys.stdin.readline().rstrip().split()))

def BS(start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == S:
            return mid
        if array[mid] > S:
            end = mid-1
            continue
        if array[mid] < S:
            start = mid+1
            continue
        

    return False
array.sort()
result = BS(0,N-1)
if result == False:
    print('찾는 원소 없음')
else:
    print(result+1) 
