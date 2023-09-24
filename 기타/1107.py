import sys
#다시 풀어보기
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
min_num = abs(100-n)
if m == 0:
    print(0)
else:
    broken = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(1000001):
        num = str(i)
        for j in range(len(num)):
            if int(num[j]) in broken:
                break
            elif j == len(num)-1:
                min_num = min(min_num,abs(int(num)-n)+len(num))
    print(min_num)  