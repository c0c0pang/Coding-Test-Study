import sys

N = int(sys.stdin.readline().rstrip())

array = [
    int(sys.stdin.readline().rstrip())
    for _ in range(N)
]

new_array = sorted(array,reverse=True)

for i in range(N):
    print(new_array[i],end=' ')