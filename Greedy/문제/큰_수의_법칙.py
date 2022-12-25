import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split());

box = list(map(int,sys.stdin.readline().rstrip().split()));

box.sort(reverse=True);

Sum = 0;

for i in range(1,M+1):
    if(i % (K+1) ==0):
        Sum += box[1];
        continue;
    
    Sum += box[0];
    
print(Sum);
