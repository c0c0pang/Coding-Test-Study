import sys
input = sys.stdin.readline

n = int(input())
LEN = 3
max_num = [0]*LEN
min_num = [0]*LEN
for i in range(n):
    down = list(map(int,input().split()))
    if i==0:
        for i in range(LEN):
            max_num[i] = down[i]
            min_num[i] = down[i]
        continue
    max_result = [max(down[0]+max_num[0],down[0]+max_num[1]), max(down[1]+max_num[0],down[1]+max_num[1],down[1]+max_num[2]), max(down[2]+max_num[1],down[2]+max_num[2])]
    min_result = [min(down[0]+min_num[0],down[0]+min_num[1]), min(down[1]+min_num[0],down[1]+min_num[1],down[1]+min_num[2]), min(down[2]+min_num[1],down[2]+min_num[2])]
    for i in range(LEN):
        max_num[i] = max_result[i]
        min_num[i] = min_result[i]

print(max(max_num),min(min_num))
