import sys
import heapq
n = int(sys.stdin.readline().rstrip())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
