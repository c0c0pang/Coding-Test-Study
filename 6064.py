import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().rstrip().split())
    sm,sn = x,0
    cnt = x
    for _ in range(x):
        sn+=1
        if sn>n:
            sn=1
    w = sn
    check = True
    while sn!=y:
        sn+=m
        if sn>n:
            sn%=n
            if sn==0:
                sn=n
        cnt+=m
        if w==sn:
            check = False
            break
    if check:
        print(cnt)
    else:
        print(-1)