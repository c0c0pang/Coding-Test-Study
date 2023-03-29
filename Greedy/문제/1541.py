import sys
sys_input = sys.stdin.readline
box = sys.stdin.readline().strip().split('-')
array =[]
for i in box:
    array.append(i.split('+'))
result = 0
for j in range(len(array)):
    sum_num = 0
    for z in range(len(array[j])):
        if array[j][z]=='' and len(array)==1:
            continue
        if array[j][z]=='':
            continue
        sum_num+=int(array[j][z])
    if j>0:
        sum_num*=-1
    result+=sum_num
print(result)