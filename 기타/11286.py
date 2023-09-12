import sys
from queue import PriorityQueue
n = int(sys.stdin.readline().rstrip())
que = PriorityQueue()
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x==0:
        if que.empty():
            print(0)
        else:
            print(que.get()[1])
    else:
        que.put((abs(x),x))
    