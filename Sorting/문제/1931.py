import sys

cnt = 0

n = int(sys.stdin.readline().rstrip())
array = []
for _ in range(n):
    f, s = map(int, sys.stdin.readline().rstrip().split())
    array.append([f, s])
array.sort()
array.sort(key=lambda x: x[1])
f_x = array[0][0]
f_y = array[0][1]
cnt = 1
for i in range(1, n):
    if array[i][0] == array[i][1]:
        cnt += 1
        f_y = array[i][0]
    elif f_y <= array[i][0]:
        cnt += 1
        f_y = array[i][1]

print(cnt)
