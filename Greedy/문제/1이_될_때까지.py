import sys

N,K = map(int,sys.stdin.readline().rstrip().split());

count = 0;

while True:
    if(N==1):
        break;
    if(N%K==0):
        N = int(N/K);
        count +=1;
    else:
        N -= 1;
        count +=1;
    

print(count);