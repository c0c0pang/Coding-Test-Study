import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
q = []
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
heapq.heapify(arr)
result=[]
while len(arr) !=1:
    n1 = heapq.heappop(arr)
    n2 = heapq.heappop(arr)
    sum_num = n1+n2
    heapq.heappush(arr,sum_num)
    result.append(sum_num)
        
print(sum(result))



