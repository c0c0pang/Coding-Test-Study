import sys
from functools import cmp_to_key
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
q = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
arr.sort()
heapq.heappush(q,arr[0][1])
for i in range(1,n):
    if(q[0]<=arr[i][0]):
        heapq.heappop(q)
    heapq.heappush(q,arr[i][1])

print(len(q))
