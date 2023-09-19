import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    mbti = list(sys.stdin.readline().rstrip().split())
    if n<33:
        min_num = sys.maxsize
        for i in range(n):
            for j in range(i+1,n):
                for z in range(j+1,n):
                    cnt = 0
                    for a,b in zip(mbti[i],mbti[j]):
                        if a!=b:
                            cnt+=1
                    for b,c in zip(mbti[j],mbti[z]):
                        if b!=c:
                            cnt+=1
                    for c,a in zip(mbti[z],mbti[i]):
                        if c!=a:
                            cnt+=1
                    min_num = min(cnt,min_num)
        print(min_num)
    else:
        print(0)
   