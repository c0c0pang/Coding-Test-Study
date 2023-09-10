import sys

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

s = sys.stdin.readline().rstrip()

i,cnt,result = 0,0,0

while i<m-1:
    if s[i:i+3] =='IOI':
        i+=2
        cnt+=1
        if cnt==n:
            result+=1
            cnt-=1 # 연속되니깐 -1만 감소시키면 됨
    else:
        i+=1
        cnt=0
print(result)