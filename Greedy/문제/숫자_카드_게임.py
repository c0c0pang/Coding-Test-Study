import sys

N,M = map(int,sys.stdin.readline().rstrip().split());

box = [
    list(map(int,sys.stdin.readline().rstrip().split()))
    for _ in range(N)
]
MINNUM  = 0;
for i in range(N):
    if(MINNUM<min(box[i])):   
        MINNUM = min(box[i]);
        
print(MINNUM);
    