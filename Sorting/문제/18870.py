import sys

n = int(sys.stdin.readline().rstrip())


def BS(start, end, target):
    global mid
    mid = 0
    while start <= end:
        mid = (start+end)//2
        if sort_array[mid] == target:
            break
        if sort_array[mid] > target:
            end = mid - 1
            continue
        if sort_array[mid] < target:
            start = mid + 1
            continue
    return mid


array = list(map(int, sys.stdin.readline().rstrip().split()))

sort_array = sorted(list(set((array))))

index = []
for j in sort_array:
    index.append(j)

for z in array:
    print(BS(0, len(sort_array), z), end=" ")
