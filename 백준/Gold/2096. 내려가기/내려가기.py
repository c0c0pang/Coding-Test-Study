import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
max_num = arr
min_num = arr
for i in range(1,n):
    x,y,z = map(int,input().split())
    max_num = [max(max_num[0]+x,max_num[1]+x),max(max_num[0]+y,max_num[1]+y,max_num[2]+y),max(max_num[1]+z,max_num[2]+z)]
    min_num = [min(min_num[0]+x,min_num[1]+x),min(min_num[0]+y,min_num[1]+y,min_num[2]+y),min(min_num[1]+z,min_num[2]+z)]
print(max(max_num),min(min_num))
