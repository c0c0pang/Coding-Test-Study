import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

array = list(map(int,sys.stdin.readline().rstrip().split()))
num = 1000000000

def BS(target,start,end):
    result =0
    while start<=end:
        cnt = 0
        mid = (start+end)//2
        for i in array:
            if i>=mid:
                cnt += i-mid
        if cnt == target:
            return mid
        if cnt <target:
            end = mid - 1
            continue
        if cnt > target:
            start = mid +1
            result = mid
            continue
    return result
array.sort()
print(BS(M,0,num))
            