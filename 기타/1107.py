import sys
#다시 풀어보기
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
min_num = abs(100-n)
if m!=0:
    broken = list(sys.stdin.readline().rstrip().split())
else:
    broken = []
for i in range(1000001):
    num = str(i)
    for j in num:
        if j in broken:
            break
    else:
        min_num = min(min_num,abs(i-n)+len(num))
print(min_num)  