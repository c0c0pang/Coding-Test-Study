import sys
input = sys.stdin.readline
n = int(input())
dic = {}
array = []
num = 9
d = 10;
for i in range(n):
    arr = list(input().strip())
    array.append((len(arr),arr))
    
array.sort(reverse=True)
answer = 0

for i in array:
    w,str_arr = i
    for j in range(w):
        if(dic.get(str_arr[j])):
            dic[str_arr[j]]+= pow(10,(w-j-1))
            continue
        dic[str_arr[j]] = pow(10,(w-j-1))
result = []
for i in dic.values():
    result.append(i)
result.sort(reverse=True)

for i in result:
    answer+= i*num
    num-=1
print(answer)

      